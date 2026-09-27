# Church in Conversation — Website V2 Storyboard

**Status: FROZEN — Mark, 2026-09-02 ("Freeze it"). Companion to
`CiC_Website_Design_V2.md` (the design record — philosophy, system, rulings).
Reviewed by Opus the same day (`Sandbox/D2-struggle/D3-synthesis-review.md`:
ready to freeze with eleven named fixes); applied in this revision, each
named where it lands, and spot-checked against the review's own list before
the freeze. From here, changes need a change order (`Decision-Log.md`), not
quiet edits — this file and its companion design record are the binding
reference for D4. Its own ⚠ items and Appendix A's draft-copy lines are not
resolved by the freeze — they're real open decisions for D4 or sooner. Not
built; nothing here is live.**

**What this is.** Every page the site has, page by page: its purpose, its
sections in order with the copy and the copy's register, every meaningful
state it has, what a screen reader encounters and the keyboard and touch
paths, and how it behaves at the constitution's breakpoints. The reference
implementation for the two rebuilt surfaces is the defended hybrid
(`Sandbox/D1-directions/06-hybrid-open-door/homepage.html` and
`tradition-chloe.html`) with the fixes the design record's §12 verified; this
storyboard is the specification a build follows, and the copy list Mark
approves from.

**Conventions.** The copy tags and decision markers are the design record's
§0. Two provenance tags are added here for material that document uses only
by reference:

- `[CAPTURE — verbatim]` — the shipped conversation capture
  `cic-website/assets/tour-captures/theon-confidence.png` (2026-08-25),
  transcribed word for word (verified against the image).
- `[BRIEF — the tradition's reviewer's brief, arranged]` — that tradition's
  brief for outside reviewers in `Build/Ministry/Scholarly-Review/`, arranged as a
  table or list, its words unchanged. For Chloe:
  `CiC_World1_Brief_for_Reviewers_Source.md` (the source of
  `CiC_World1_Brief_for_Reviewers_V0_1_DRAFT.docx`; Direction 03 used it
  first). Three more exist — `CiC_WorldBrief_Desert_V0_1_DRAFT.md`,
  `CiC_WorldBrief_Hieronymian_V0_1_DRAFT.md` (the Bethlehem Circle),
  `CiC_WorldBrief_Syriac_V0_1_DRAFT.md`; **Alexandria, the Cappadocian
  Churches and Church and Empire have none.** All four are drafts, cleared
  for no participant surface: **ruling 36** gates them, tradition by
  tradition, alongside rulings 2, 3 and 4 (the review's R7).

**Every line marked `[DRAFT COPY — pending Mark's approval]` is collected in
Appendix A for his approval pass.** Rulings are cited by their number in the
design record's §10 ("ruling 13").

**Measurements** are from the design record's §12 (Chromium, fallback faces,
sandbox note stripped unless stated).

---

## Site map

```
Home (index.html)
├── The chairs, by era → a tradition page → the app (interview)  ·  Set your own table → table.html (NEW, change order 2026-09-03)
├── traditions/<census-id>.html  ×7  (one template; Chloe's page is the reference)
│     └── "Bring {Name} to the Table" → table.html?worlds=<census-id> (NEW, same change order)
├── table.html (NEW) → the app (Table field, ≥2 seated)
├── About (about.html)
├── What's Next (whats-next.html)
├── Map = Church in History (atlas-v3.html — its own rework track)
├── Get Involved (support.html)
├── Privacy (privacy.html)  ·  Feedback (pilot-feedback.html)  ·  Contact (mailto)
├── 404.html (new)
└── unlinked, unchanged: tour.html · atlas.html → · world-atlas.html → (redirects)
```

Nav (every page): Home · About · What's Next · Map · Get Involved.
Footer (every page): About · Feedback · Privacy · Contact.

---

## S. Shared chrome — every page

### S.1 Skip link

First element in the DOM. `Skip to content` `[LIVE — carried unchanged]`.
Off-screen until focused; focused, it sits fixed at the top left on ink with
parchment text. Activating it moves focus into `<main>`; the next Tab lands on
the page's first control (homepage, as of the 2026-09-03 redesign: the
first chair's portrait link, Chloe's).

### S.2 Header

**Anatomy, left to right, wrapping:** the wordmark **Church *in* Conversation**
(a link to Home; `[VERBATIM — locked, Brand Guidelines]` — Alegreya 700, the
*in* italic 400, no "The"); the site nav, five text links; for a returning
visitor only, the side door.

| Element | Copy | Register |
|---|---|---|
| Wordmark | Church *in* Conversation | `[VERBATIM — locked, Brand Guidelines]` |
| Nav | Home · About · What's Next · Map · Get Involved | `[LIVE — carried unchanged]` |
| Side door (returning visitors only) | Been here before? Go straight to a conversation → | `[DRAFT COPY — pending Mark's approval]` |
| Side door, ≤640px | Go straight to a conversation → | (the long half hidden) |

**Rules.** The mark is not in the header (ruling 8). Nothing is sticky. The
header wraps; it never clips a link and never hides a scroller. Nav links are
≥44px targets (measured 48px tall on phones, 49px from 700) with a 2px madder
underline on hover, focus and `aria-current="page"`. Below 640px the nav sets
at .9rem with tighter gaps (design record §12). The side door is italic, muted, never a button; it is
`hidden` unless the returning flag is set, and `.site-nav a[hidden]` is
`display:none` (the inline-flex rule would otherwise defeat the attribute —
design record §11.6); a 0.3em `gap` on the anchor keeps the space between its
two halves (measured 4.55px).

**States.** *First visit:* no side door; header **163px** at 320–390 (the
wordmark on its own row above two nav rows), **114px** at 414–480 (above one
nav row), **65px** at 640 and **73px** from 700 (one row) — sandbox note
stripped; the first issue's 110 / 61 / 41 were these heights minus the
note's, corrected at the fix pass (design record §4.2, §12). *Returning*
(the `localStorage` flag `cic-returning` is set when the visitor follows any
app link; read in `try/catch`): the side door appears in the nav and costs a
row from 414 to 900 (measured: 163px at 414–480, 114 at 640, 174 at 700,
125 at 768–900; 73 from 1024). *No JavaScript:* the side door stays hidden
(the attribute is in the markup); everything else is static. *Dark:* surface ground, text `#F1E9DD`,
underline `#E08C74`. *Print:* hidden.

**Screen reader.** `banner` → link "Church in Conversation" → navigation
"Site": five links (+ "Been here before? Go straight to a conversation" when returning).
**Keyboard:** wordmark, then the five links in order, then the side door.

### S.3 Footer

| Copy | Register |
|---|---|
| © 2026 Church in Conversation. A safe space to explore faith and the story of Jesus, part of Faithways Studio, Inc. | `[LIVE — carried unchanged]` |
| About · Feedback · Privacy · Contact | `[LIVE — carried unchanged]` |

RECOMMENDED: this one footer line on every page. Today `support.html` carries
a different line ("A ministry in formation.") and `pilot-feedback.html`'s
footer nav omits Feedback and Privacy — both unify to the standard footer.
Mark to confirm the entity line as the single footer line (it is the line
the entity facts favour) — **ruling 39** in the design record's register.
Footer links are 44px targets in muted ink.

### S.4 The sandbox note

The hybrid files carry a one-line "Sandbox mockup" note above the header
(53px at 390). **It does not ship.** Every fold figure in the design record
is given with it stripped.

### S.5 Global states, every page

- **Without JavaScript:** every page complete — names, links, sections, forms
  in static markup; what degrades is named per page.
- **Reduced motion:** the mark still, seated; nothing else ever moved.
- **Dark register:** the design record's §6.2 table, one register site-wide,
  by `prefers-color-scheme` (no toggle in V2; the Atlas's own toggle is that
  track's).
- **Print:** header, skip link, support slot and any action bar hidden;
  content in order; sidenotes in flow.
- **The app unreachable** (the engine is a separate deploy on Render): the
  site cannot know; every app link is a plain link and the app's own
  loading/error states apply. No site copy promises availability.
- **404:** §9.

### S.6 Page titles and descriptions

The strings a search result, a browser tab or a shared link shows. The live
site carries both on every page in one form — `X — Church in Conversation`
— and both are participant-facing copy under the draft-and-approve rule
(the review's R10). There is no OG / Twitter-card convention on the live
site to inherit, so none is added.

| Page | `<title>` | `<meta name="description">` | Register |
|---|---|---|---|
| Home | Church in Conversation: The First Centuries | Twenty centuries of the Church's story, one era at a time. Christian traditions you can sit down with today, each with its own voice. Come and join us at the Table. | `[LIVE]` — 2026-09-03 change order: dropped the exact tradition count and named eras, both of which will go stale as more are built |
| Tradition ×7 | {Tradition} — Church in Conversation *(Chloe's: The House-Churches — Church in Conversation)* | Pattern: {Name} is a representative voice for {the tradition, as its tile names it}, {dates}. Where the record is quiet, the questions people bring, and what {she/he} is built from. *Chloe's instance:* Chloe is a representative voice for the house-churches of Antioch, Asia Minor and Rome, 70–200 CE. Where the record is quiet, the questions people bring, and what she is built from. *Theon's instance:* Theon is a representative voice for the school and church of Alexandria, c. 150 to 400 CE. Where the record is quiet, the questions people bring, and what he is built from. | title `[CENSUS — verbatim]` + the live suffix; description `[DRAFT COPY — pending Mark's approval]` — the pattern here, one instance drafted with each page as it clears ruling 4. 2026-09-03 change order: "an AI voice" → "a representative voice," matching the fleet-wide wording fix (design record §3.7 item 8) |
| About · Get Involved · Privacy · Pilot Feedback · Church in History (and its two redirect stubs) | live | live | `[LIVE — carried unchanged]` |
| What's Next | What's Next — Church in Conversation | ⚠ the live description says "three new worlds in development" — **ruling 37** | title `[LIVE]`; description is Mark's |
| 404 | Nothing at this address — Church in Conversation | There's nothing at this address. The door is still open — start with your question on the home page. — plus `<meta name="robots" content="noindex">`, since Cloudflare Pages serves the page with a 404 status and it should never be indexed | `[DRAFT COPY — pending Mark's approval]` (both) |

---

## 1. Home — `index.html`

**Purpose.** Take what the visitor brought. Open with the hook; then who
can carry it — the chairs, by era; then two picture-led portals (the
Table, then the map, the map last as the closing door before the ask);
then the ask. *(Order corrected 2026-09-08 — see §1.6's own amendment
for the reasoning.)*

**History, most recent first (Decision-Log has the full reasoning for
each):**
- **2026-09-03, latest.** Mark, on seeing the shipped cuts: right
  elements, wrong graphics. Three changes: (1) the era gallery goes from
  one-open-at-a-time (an accordion the previous entry below describes,
  in place for under an hour) to two eras always visible as rows, each
  scrollable sideways for chairs that don't fit, with a vertical scroll
  once a third era exists — see §1.3's own section below for the
  mechanism. (2) Church in History gains an actual picture of the
  Atlas — a screenshot of its own timeline map — instead of describing
  it in words alone. (3) The Table teaser gains the painted three-
  representatives-at-a-table image already used for the Get Involved
  page's giving asks (`Build/Ministry/Communication/Brand-Assets/Table-
  Templates/Open Door Table Image.png`). Both images now anchor a
  "portal" card — picture, then a short pitch, then the link — replacing
  the old text-only `.map` section and the `.second-door` paragraph that
  used to live inside §1.3.
- **2026-09-03, later.** §1.2 ("Start with your question" — the input
  box and the six offered questions) is cut entire, not just trimmed.
  It was a second way in alongside the chairs, and Mark's read going
  through this freeze pass was that the chairs are the one path that
  matters now; a typed-question door duplicated it. The one disclosure
  line the door section carried (representative voice, not a person who
  lived) moved into §1.3, right after the scope line, so it isn't lost.
  The held-question mechanism (`#q=`, ruling 14) has no producer on the
  homepage anymore; each tradition page's own `#q=` handling is
  untouched and still works if a link ever arrives carrying one.
- **2026-09-03, earlier the same day.** The sample exchange (old §1.4)
  and the two-column disclosure grid (old §1.5) cut entire — explanation
  about the experience, not the experience, and a distraction. Numbers
  describing the current build state (how many traditions, how many
  eras) also swept out of the homepage's copy — they'll be stale within
  weeks. See the fuller note this replaced, preserved in the
  Decision-Log rather than repeated here.
- **2026-09-02.** §1.2 and §1.3 swapped order (before today's cut, §1.2
  came first): a visitor should meet who's there before being handed a
  bare question box. Moot now that §1.2 is gone, but recorded since it's
  why §1.3 is a gallery grouped by era rather than a stacked list — that
  part of the ruling still stands.

**Order of the page (H-level outline), current:** H1 hook → §1.3 H2 *Who
would you like to have a conversation with?* (H3 era, one per era, each a
toggle; H4 name × however many are built) → §1.4 H2 *Church in History* →
§1.5 H2 *Support* (visually hidden). No skipped levels (verified against
the build). Section numbers below haven't been renumbered to match —
they still read §1.3 / §1.6 / §1.7 for the sections that survive, since
renumbering a frozen document's own cross-references for their own sake
isn't worth doing until the next real content change touches them.

**Data.** The seven chairs are the census's own fields. RECOMMENDED: generate
the seven rows into the static HTML from `world-census.json` by a small
script run before commit (the census stays the single source; the page stays
static and complete without JavaScript — the 02 defense's DOM-as-document
law), rather than the live site's runtime `fetch` (which renders nothing
without JavaScript and nothing on a fetch failure). The page carries a
comment naming the census version it was generated from.

### 1.1 Hero

| # | Element | Copy | Register |
|---|---|---|---|
| 1.1a | The mark, 52px (44px on phones), plays once on arrival (§6.3 of the design record; ruling 16); `aria-hidden` | — | — |
| 1.1b | The mark's public sentence, caption size, beside the mark | The mark is a table; the opening is the way in — and it never closes. | `[VERBATIM — locked, Brand Guidelines]` |
| 1.1c | H1 | Twenty centuries of the Church. One table. A chair pulled out for you. | `[VERBATIM — locked, Brand Guidelines]` |
| 1.1d | Welcome-back line (returning visitors only; hidden otherwise) | Welcome back. Go straight to a conversation → | `[DRAFT COPY — pending Mark's approval]` |

The first text on the page is the mark's sentence — the Logo Usage Sheet's
caption rule discharged, an explicit choice (ruling 8). Centred; the H1 at
`clamp(2rem, 4.5vw, 3rem)`, weight 500.

### 1.2 The door

The page's first surface and its only filled control. A vellum box with a
hairline border; inside it, top to bottom:

**Removed, 2026-09-03.** Every element that lived here (the input, the
"Choose who to ask" control, the lede, the "how" line, the six offered
questions and their note) is cut along with the section. The one line
that has to survive — the representative-voice disclosure — moved to
§1.3, right after the scope line. The held-question mechanism (`#q=`,
ruling 14, ruling 30's no-query-string rule) no longer has anything on
the homepage that produces one; a tradition page reached by a link that
already carries `#q=` still reads and forwards it correctly, unchanged.

### 1.3 Who would you like to have a conversation with — `#who`

**Now the first screen after the hero.** Top to bottom:

**The chairs are a gallery, not a stacked list (2026-09-02 change order):**
each era heading is followed by a grid, `repeat(auto-fill, minmax(150px,1fr))`,
so an era's chairs run left to right in chronological order and the next
era starts a new row below — vertical position reads as time, horizontal
position within a row reads as chronology within that era. This is the
scale answer for "more than ten": a new tradition joins its era's row
(wrapping to a second row under the same era heading if the row is full)
rather than lengthening a single column everyone has to scroll past.
Portrait, name, role, tradition, dates, and the chair action (§1.3h)
are unchanged; the descriptive tile sentence (§1.3f's `entry.tile`) is
still full census-verbatim text in the DOM, `-webkit-line-clamp: 2` for
sighted layout only — a screen reader still hears the whole sentence.

**Two eras always visible; each era's own row scrolls sideways for
chairs that don't fit (2026-09-03 change order, replacing the same-day
accordion above, which Mark reversed within the hour on seeing it
shipped):** the era heading is a plain heading again, no toggle. Each
era's chairs are a single-row flexbox (`display:flex`, no wrap,
`overflow-x:auto`), card width fixed at 232px regardless of viewport —
Mark's instruction was explicitly not to shrink cards to fit more in,
so overflow scrolls instead of the cards shrinking. `#who-gallery`
itself caps its height to exactly the combined height of the first two
`.era-group` elements once a third era exists (`sizeGallery()`, measured
from real rendered height, recomputed on resize) and scrolls vertically
for eras beyond the second; with today's two eras there is nothing to
cap, so no vertical scroll shows yet. No-JS: the height cap never
applies (all eras show, stacked, however many exist) and each era's
horizontal scroll still works — it's plain CSS, no script needed.
**Build note:** `.chairs{overflow-x:auto}` on a `display:flex` row
leaked its own unclipped content width into `document.documentElement`'s
scrollWidth even though it rendered correctly clipped — a real, empirically-
confirmed Chromium sizing quirk, not a misunderstanding of the CSS.
Fixed with `contain:layout` on `.chairs`, which isolates the row's
internal layout from affecting any ancestor's size calculations;
verified zero overflow 320–1440px, light and dark, before and after.

| # | Element | Copy | Register |
|---|---|---|---|
| 1.3a | *Removed 2026-09-03* — the held block had no producer once §1.2 was cut; see §1.2's own removal note | — | — |
| 1.3b | Eyebrow | Who's at the table | `[LIVE — carried unchanged]` |
| 1.3c | H2 | Who would you like to have a conversation with? | `[DRAFT COPY — pending Mark's approval]` — 2026-09-03 change order (Mark): the project's name is *Church in Conversation*; a question is how one starts, but the conversation is the point, and the heading should say so |
| 1.3d | Scope line (carries the sentence the hero gave up) | Christian traditions from the Church's first four centuries, each with one voice that speaks for it from its own letters and records. Ask any of them. | `[LIVE]` — 2026-09-03 change orders: dropped "Seven" (a count that changes as more traditions are built) and "You can bring the same question to more than one" (the held-question feature it referred to no longer exists on this page) |
| 1.3d′ | The representative-voice line, relocated here from the removed §1.2g when that section was cut | You will be in conversation with a representative voice, not a person who lived — built from one tradition's own letters and records, and honest about where they run out. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3e | Era heading, H3, one per era, plain (2026-09-03: no longer a toggle — see the gallery mechanism above) | The Early Church Era · 70–312 CE / The Imperial Church Era · 312–451 CE | `[CENSUS — verbatim]` (the census's era heads carry hyphens; the dash seam is a data fix — design record §11.3) |
| 1.3f | The chairs (see the table below), each era's own horizontally-scrolling row — each an `<li>`: 72px portrait in a 2px tint ring, portrait itself a link, fixed 232px card width, H4 name with the role beside it in muted sans · tradition name in italic · dates · region in sans · the tile · one text action | — | `[CENSUS — verbatim]` |
| 1.3h | Chair action (muted text link; the portrait links to the same place, so this isn't a second path in) | Her/His record → *(visually hidden: " — {Tradition}")* | `[DRAFT COPY — pending Mark's approval]` (pattern) — present on all seven as of 2026-09-03. The direct "Ask {Name} →" shortcut that used to sit beside it was removed the same day: one path into each tradition (portrait or record link → the tradition page → the actual interview/table launch), not two |
| 1.3i | Pilot note — **below the seven**, the live site's own order | This is a pilot. We're intentionally looking for a limited number of participants across four perspectives — general, pastor or teacher, academic, and anyone re-examining their faith. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3j | Cost caveat — below the seven | Because of cost, we're asking each participant to keep to about five conversations for now — we can't enforce this yet, only ask. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3i′/j′ | **Offered re-draft for ruling 20** (replaces 1.3i–j if Mark takes it) | This is a pilot. We're listening for what people coming from four directions find here — the curious, pastors and teachers, scholars, and anyone re-examining their faith. Every conversation costs real money to run, so for now we ask each person to keep to about five. We can't enforce that; we can only ask. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3k | *Moved 2026-09-03* — the second door left §1.3 for its own picture-led portal card; see §1.6 below. The Arriving mark (`id="table-cue"`) moved with it, unchanged otherwise. | — | — |

**The seven chairs — every field from `world-census.json` (2026-09-02), rendered verbatim:**

| Order | Census id (deep link) | Name · role | Tradition | Dates · region (as the data has it) | Tint light / dark (proposed, ruling 7) | Portrait | Record page |
|---|---|---|---|---|---|---|---|
| 1 | `post-apostolic-house-church` | Chloe · Household Leader | The House-Churches | `70–200 CE` · Antioch, Asia Minor, Rome | `#7c3aed` / `#955FF0` | `house-churches.png` | reference page exists |
| 2 | `alexandria-catechetical` | Theon · Catechetical Teacher | Alexandrian Christianity | `c. 150–400 CE` · Alexandria, Egypt | `#2B5F8A` / `#3B83BF` | `alexandria.png` | template |
| 3 | `syriac-edessa-nisibis` | Mar Yausep · Teacher of the Covenant Order | Syriac Christianity | `200–410 CE` · Edessa & Nisibis | `#b45309` / `#CC5E0A` | `syriac.png` | template |
| 4 | `imperial-juridical-christianity` | Marius · Deacon of the Letters | Church and Empire | `c. 312-451` (hyphen, no era marker — data seam) · Rome, Constantinople, Milan | `#7A2E2E` / `#C36060` | `empire.png` | template |
| 5 | `desert-monasticism` | Papnoute · Abba (Elder) | Desert Fathers and Mothers | `c. 320–430 CE` · Nile Valley & Desert, Egypt | `#0f766e` / `#128D84` | `desert.png` | template |
| 6 | `cappadocian-nicene-pastoral-monastic-tradition` | Chilo · Elder of the Brotherhoods | The Cappadocian Churches | `c. 325-394 CE` (hyphen — data seam) · Cappadocia / Anatolia | `#A0522D` / `#C46437` | `cappadocian.jpg` | template |
| 7 | `hieronymian-ascetic-literary` | Albina · Widow of the Household | The Bethlehem Circle | `c. 382–420 CE` · Rome & Bethlehem | `#9d174d` / `#E23B7F` | `bethlehem.png` | template |

Order is by the census `start` field (chronological), grouped under the two
era heads. The tile under each chair is the census `entry.tile`, verbatim.
"Mar Yausep" is never split (the honorific is part of the name — Mark's
2026-08-28 identity ruling, carried from the live site's own code comment).

**On phone, first load:** the landing screen reads — Who's at the table ·
Who would you like to have a conversation with? · scope · the
representative-voice line · The Early Church Era, with Chloe's chair
inside it. No pilot paragraph, no cost paragraph in the landing zone; no
held-question state exists on this page anymore (§1.2 removal, above).

### 1.4 / 1.5 — removed, 2026-09-03

Both sections (the sample exchange and the two-column disclosure block)
are cut from the homepage; see the change order under "Purpose" above.
Two of this section's locked brand lines (1.5n, 1.5o — "We are committed
to representing each Christian movement in full..." / "We measure
whether each Christian movement is represented...") moved to About's
mission section, right after its own closing paragraph — resolved the
same day, not left open.

### 1.6 Church in History — one link

~~**2026-09-03 change order: merged with the Table teaser into two
picture-led "portal" cards, full width, stacked (Atlas over Table).**~~
Each is one `<a>` wrapping an image, then an eyebrow, an H2, a short
paragraph, and a CTA line — click anywhere on the card. Mark's own call
after seeing both laid out: side by side at half-width, the Atlas image
read as a blurry smudge — full width was the only way the picture
actually did its job. Ruling 23 ("no map band") was about not building
a new interactive map widget into the homepage before the Atlas rework
lands; a static image linking to the shipped Atlas isn't that.

**Amendment, 2026-09-08 — stacking order reversed on newer research,
not on the full-width call above (which stands).** The shipped page
was actually built Table-then-Atlas, the opposite of the 2026-09-03
ruling's stated "Atlas over Table" — an implementation gap this
document never caught. Rather than silently conforming the code to the
stale ruling, Mark asked to "follow the most current data and
research": `Build/Ministry/Features/Website-V2/Research/05-landing-page-
structure-and-choice-flow.md` finds real precedent (guided-then-explore
structures across museum and interactive-journalism sites, "generous
interfaces" research) for free exploration as the closing *coda* to a
guided path, not a competing option stacked earlier. Table stays the
second, quieter door right after the chairs; the Atlas portal becomes
the last thing before the ask. The struck ruling above is kept, not
deleted, so the original reasoning (image legibility at full width)
stays on record — only the stacking order it also specified is
superseded, per newer evidence.

**Portal 1's image is not a screenshot of the live `atlas-v3.html`.**
It's a captured frame of `river-prototype.html`, the in-progress
visual-language rework on the separate `claude/atlas-game-grade-
visuals` branch (Build/Ministry/Features/Atlas-World-Map/Design/) — flowing
colored "rivers" per tradition family instead of the shipped page's
straight boxed lines. Mark named that branch directly ("the new sandbox
version we are building") and separately corrected the era-band
background from that branch's own tan/sage/blue tri-tone to plain
white — a design decision made in conversation, not yet committed to
that branch's own file, applied here only to the captured image. The
portal's CTA still links to `atlas-v3.html`, the page that actually
ships today; the picture is deliberately ahead of what a click currently
lands on. That gap is a known, chosen thing, not an oversight — worth
closing when the rework itself ships, not before.

| # | Element | Copy | Register |
|---|---|---|---|
| 1.6a | Portal 1 image — a captured frame of the river-prototype visualization (era-band background changed from tan/sage/blue to white per Mark's correction), cropped to 1200×655, `assets/atlas-preview.jpg` | — | `[LIVE]` — real capture of an in-progress prototype, not a mockup; not what `atlas-v3.html` looks like today |
| 1.6b | Portal 1 eyebrow | Twenty centuries on one map | `[DRAFT COPY — pending Mark's approval]` |
| 1.6c | Portal 1 H2 | Church in History | `[LIVE — carried unchanged]` (the Atlas's own name) |
| 1.6d | Portal 1 paragraph | More traditions are chosen and being built all the time. Christian movements across the Church's whole history are on record in the project's map — hover for a glimpse, click for depth. | `[LIVE]` — trimmed further for the card's shorter format; the "what is not yet built is still there to be read" clause moved to the What's Next line below |
| 1.6e | Portal 1 CTA | Open Church in History → | `[DRAFT COPY — pending Mark's approval]` |
| 1.6f | Portal 2 image — the painted three-representatives-at-a-table piece already used on Get Involved's giving asks (`Build/Ministry/Communication/Brand-Assets/Table-Templates/Open Door Table Image.png`, resized to 1200×655), `assets/table-portrait.jpg` | — | `[LIVE]` — reused brand art, not new |
| 1.6g | Portal 2 eyebrow | The Table | `[DRAFT COPY — pending Mark's approval]` |
| 1.6h | Portal 2 H2 | Set your own table | `[DRAFT COPY — pending Mark's approval]` |
| 1.6i | Portal 2 paragraph | Bring two or three of them to one table. No one seated there is the host — you're one of the four chairs. | `[DRAFT COPY — pending Mark's approval]` — replaces old 1.3k's single line, expanded since the card has room for it |
| 1.6j | Portal 2 CTA, carrying the Arriving mark (moved from old 1.3k, unchanged) | Set your own table → | `[DRAFT COPY — pending Mark's approval]` |
| 1.6k | Secondary link, below both cards, own line | What's next → | `[DRAFT COPY — pending Mark's approval]` |

### 1.7 The support slot

A content slot in the quietest register — sans, muted, text links, below
everything (D0 seam F: the cost/ask copy was rewritten six times in one
week; nothing in the layout depends on its wording).

| # | Copy | Register |
|---|---|---|
| 1.7a | H2 (visually hidden): Support | `[DRAFT COPY — pending Mark's approval]` |
| 1.7b | Running these conversations costs real money. If you'd like to help more people use them: | `[LIVE — carried unchanged]` |
| 1.7c | Keeping the Door Open — give once · Open the Door Wider — give monthly | `[LIVE — carried unchanged]` (the two Stripe links, as text links, never buttons here) |
| 1.7d | For what this actually costs and where it goes, see Get Involved. | `[LIVE — carried unchanged]` |

### 1.8 States

| State | What the visitor sees |
|---|---|
| **First visit** | No side door, no welcome-back line. Hook, chairs (first era open), the representative-voice line above them. |
| **Returning** (flag set) | The side door in the header; *Welcome back. Go straight to a conversation →* under the hook. Everything else identical — chairs don't move, never in a carousel. |
| **Launch state** (ruling 4) | All built tradition pages exist and every chair carries the same single record link into its page — one path in, not the "Ask" shortcut plus record link this table originally planned for. This is the shipped shape §1.9 describes now, not an interim one. |
| **A tradition page reached via a `#q=` link** (shared, bookmarked, or from some future source — nothing on the homepage produces one anymore since §1.2 was cut) | That page's own held block shows the question without scrolling; it forwards into that page's own "Begin a conversation" link. Unaffected by anything on this page. |
| **No JavaScript** | Era toggles have no click handler, so every era's chairs are visible, unhidden, all the time — strictly more content shown, never less. Every name and record link present. |
| **Dark** | §6.2 dark table; the tints are the `colorDark` values (rings only). |
| **Reduced motion** | The mark still, seated; nothing else moves in any state. |
| **Print** | Header, support slot, skip link hidden; every section present. |

### 1.9 Accessibility behaviour

**What a screen reader encounters, top to bottom, as of the 2026-09-03
redesign:** skip link → banner: "Church in Conversation" link, navigation
"Site" (5 links) → main → H1 (the hook) — the mark is decorative and
silent; its sentence is read as a paragraph before the H1 → H2 "Who would
you like to have a conversation with?" → scope → the representative-voice
line → per era: a plain heading, then its row of chairs, each H4 "{Name}
{Role}", tradition, dates and region, the tile, link "{Her/His} record"
(the portrait is the same link, so it isn't a second stop) → the pilot
note, the cost caveat → link "Open Church in History" (image, eyebrow,
H2, paragraph, and CTA all inside the one link) → link "Set your own
table" (same pattern) → link "What's next" → H2 "Support" (visually
hidden) → three lines with three links → contentinfo: the entity line,
four links.

**Keyboard path.** skip link → wordmark → 5 nav links (→ side door) →
[welcome-back link] → per era: each chair's portrait/record link (no
toggle stop anymore) → the Table portal link → the Church in History
portal link → What's next → give once → give monthly → Get Involved → 4
footer links. Focus ring 2px madder, 3px offset. No positive `tabindex`;
nothing hidden is a stop; nothing is sticky, so the focused element is
never obscured. Exact stop counts aren't tracked here anymore — they'd go
stale with every tradition added, exactly the kind of number the
2026-09-03 ruling says to stop carrying in this document.

**Touch.** Every control ≥44px tall: the chair links, each era's
horizontally-scrolling row itself (touch-drag, no button needed), the
two portal cards, the support links, the footer links, the nav.

### 1.10 Responsive behaviour

| Width | Behaviour |
|---|---|
| ≥900 (desktop) | Chrome at 64rem; sections at 44rem; reading at 38rem. Header one row (73px). |
| 640–899 | Single column narrows. Header one row (65px at 640, 73 from 700). |
| <640 (phone) | Header wraps — the wordmark on its own row above two nav rows at ≤390 (163px), above one at 414–480 (114px); the nav at .9rem; portrait 72px (56px ≤480); everything single column; no horizontal scroll at 320 (verified). |

Page height, after both 2026-09-03 cuts (the disclosure/exchange
sections, then §1.2): 2,755px at 390×844, 2,041 at 1280 — a bit over a
fifth of the original 9,441px/6,786px measurement this page started
the day at.

---

## 2. Tradition page — the template (reference: Chloe, `post-apostolic-house-church.html`)

**Purpose.** One tradition, one voice, one chair, reached one click from a
homepage chair or a held question — just enough to interest, orient, and
engage: what makes this world distinctive, who you'd be talking with, and
a door in. Not a paper. Wording is expected to keep changing; this shape
is the part that holds.

**URL.** `traditions/<census-id>.html`.

**Order:** breadcrumb → title block (identity line, H1, formal name,
status, one-sentence tile, portrait + a caption naming what's distinctive
about the tradition, never describing the image) → one-line representative
statement ("X is a representative voice for this tradition, not a person
who lived — built from its own letters and records, and honest about
where they run out") → held question, if any → the seat (Begin / Bring to
the Table) → who is speaking, one short paragraph naming the tradition's
own voices + the distress line → where it's quiet, one short honest-limit
statement in the tradition's own words → questions to ask, three or four,
each a link into the interview with a one-line source note → the closing
door (Begin / Bring to the Table again).

**Content sources:** identity/H1/formal name/tile/status from the census
entry; the "who is speaking" line names real voices from the census or
record store; the one quiet statement and every question's source note
trace to a real record id — quoted, never paraphrased. No sources table,
no gravities, no lexicon, no review-status apparatus — that depth lives
in the record store and, if ever wanted, in About's "how it works," not
repeated on every tradition page.

**Build files carry no comments, notes, or `data-copy`-style markers.**
Register and sourcing questions belong in the Decision-Log, never inline
in the HTML/CSS/JS.

**States:** the global states only (§S). Zero horizontal overflow
320–1440px; no `target="_blank"`; same-tab throughout.

---
---

## 2a. Set your own table — `table.html` (NEW, change order 2026-09-03)

**Not in the original storyboard.** §1's site map originally sent "Set your
own table" straight into the app's Table field, with the app's own Launch
screen doing all seat-picking (see §1.7's app-boundary note). Mark's
critique of the hybrid build: the homepage showed the multi-voice option as
a second link hanging off Chloe's card — "that gets confusing and sets
Chloe to be the leader rather than joining the conversation." Ruling: the
Table becomes its own page. No tradition is ever shown as the table's host;
"You" is one of four seats, symmetrically, the same as the three you invite.

**Purpose.** Let a visitor assemble up to three traditions before ever
opening the app, then hand the app a single ready-to-convene link
(`?worlds=id1,id2[,id3]&mode=table`) — confirmed against the app's own
`Launch.tsx` that this pre-seeds the field without auto-starting a session
("the link chooses seats, the participant convenes").

**The graphic.** Adapts the "Arriving" brand mark's own ring-and-doorway
geometry — one continuous ring, one gap, one seated dot — to four seats
instead of one, keeping the mark's own shape: a single unbroken arc (the
same "C" the logo draws), not four cut segments. The gap is a quarter of
the circle, centered on the right where "You" sits — the mark's own
threshold position, kept exactly. All four seats, "You" included, sit
just outside the ring's edge, like chairs pulled up to a round table
rather than fitted into notches cut in it; each is centered on its own
quarter of the circle, 90° apart, matching the ring's own quartering.
(First pass drew four dashed arc-segments with a gap at every seat, each
circle overlapping the ring rather than sitting outside it — Mark's
correction on seeing it: the ring should read as the logo's own single
opening, and the seats should sit at the table, not in it.) Plays once on
arrival — the ring draws, "You" settles in — under the same restraint
discipline as the homepage's own mark (§1.2's Arriving sequence): no
other motion on the page, `prefers-reduced-motion` shows the completed
state with `animation: none` explicitly set on every animated rule, not
just the resting values.

**Order of the page:** eyebrow "The Table" → H1 "Set your own table" → one
line stating no seat is host → the graphic (aria-hidden; each open seat is
a real button with a visually-hidden status span) → the AI-disclosure line
(same register as the homepage's 1.3d′ and each tradition page's own AI line) →
the convene control, disabled and reading "Choose at least two…" until two
seats are filled, then "Open the conversation" with the built `?worlds=`
link → a live seat count (`aria-live="polite"`) → the cost caveat carried
verbatim from every other conversation entry point.

**The chooser.** Clicking an open seat (or a filled one, to change it)
opens a side panel (bottom sheet under 640px) listing all seven
traditions with portrait, name, and tradition name; a tradition already
seated elsewhere is shown, disabled, "Already seated," not hidden. A
filled seat's chooser adds "← Leave this seat open" above the list. Escape
or the × returns focus to the seat button that opened it.

**Hand-off from a tradition page.** Each tradition page's "Bring {Name} to
the Table" link now points to `table.html?worlds=<census-id>`
instead of the app directly — that tradition arrives pre-seated, as one of
three open seats, not as the page's own subject. The held `#q=` question
is **not** carried onto this link: a question held for one voice
doesn't cleanly address a table where that voice is no longer singled
out, and forwarding it would re-introduce the "one tradition speaks for
the room" framing this page exists to remove. The two per-tradition
"Begin a conversation with {Name}" interview links are unaffected and
still carry `#q=` as before.

**No-JS:** the seat buttons and convene control need script to build the
`?worlds=` link from a live selection; `<noscript>` offers a plain link
straight to the app's empty Table field instead of a dead control.

**States:** the global states only (§S). **Screen reader:** banner → main
→ H1 → graphic (aria-hidden, its four buttons independently reachable) →
AI line → convene control → live seat count → contentinfo. **Keyboard:**
chrome → three seat buttons → convene control; the chooser panel traps
focus at its close button on open and returns it to the seat button on
close. **Responsive:** single column, `--col` measure throughout; the
graphic scales down at ≤480px (240px ring) with seat positions
recalculated, not just shrunk; zero horizontal overflow 320–1440px
(verified).

**Ruled 2026-09-03 — ruling 35: no gate.** The Table ships free and
prominent, as built, confirmed rather than merely assumed (Design V2's
own ruling register, item 35). **Ruled the same day — `pairings.ts` stays
out of this page for now.** Checked the actual file
(`cic-poc/frontend/src/data/pairings.ts`) before ruling rather than
assuming: it is sourced from a pairing record that itself "awaits Mark's
sign-off," three of its four curated pairings are marked `proven:false`,
one pairing is deliberately withheld from public offering pending
battery-accompanied runs, and its `worldKeys` (`alx`, `pahc`, `desert`…)
don't match the website's own census ids — reusing it here would mean
duplicating draft, partly-unproven editorial judgment across two
codebases with no shared source of truth, and risks quietly re-importing
a "curator's picks" framing this page was just rebuilt to remove. The
seven-choice picker stays the only path in this version — three taps,
and for a first-time visitor who doesn't yet know Theon from Papnoute, a
chance to see all seven traditions rather than being funneled toward a
few. Revisit once the underlying pairing record is signed off and more
of its pairings are proven, as a clearly separate, secondary affordance
("New here? Try…") — not folded into the core picker.

**Still open:** the SVG ring's gap centering is tuned by eye against the
mark's own geometry, not derived analytically — acceptable as a first
pass, refinable if Mark's reaction calls for it.

---

## 3. About — `about.html`

**Carried.** The V2 chrome (§S) replaces the live header (the mark bare,
without its sentence; the wordmark without the italic *in* — both Logo Usage
Sheet breaks). Copy carried `[LIVE — carried unchanged]` throughout: the
mission statement and its two paragraphs; the "Where we are today" callout —
with the pending count correction ("seven traditions from the Church's own
first four hundred years", Decision-Log 2026-09-02, done in a worktree, not
yet pushed); the Five Convictions; How It Works (the homepage's link target,
`#how-it-works`); Safety & Disclosure; About Us with the entity paragraph.

**What V2 changes on this page:** the chrome; the shared stylesheet's tokens
and usage layer (secondary text in ink-faded, never `--muted #6B6259`; links
madder with madder-deep hover, not gold-leaf); the convictions' numbered
madder rings stay (the live site's own device); the callout's gold-leaf left
rule stays (a rule, not text) and its label goes from gold-leaf text to ink
(gold-leaf never sets small text — design record §6.2). No new copy.

**States:** the global states only. **Screen reader:** banner → main → H1
"What everything is for" → five sections, each eyebrow + H2 + prose; the
convictions as an ordered list of H3s → contentinfo. **Keyboard:** chrome →
the two mailto links → footer. **Responsive:** single column at 40rem; no
divergence.

**Note for Mark, not a ruling:** the page says "What we believe" (the
convictions' H2) and the mission's second paragraph is the project's own
confession in its own voice. This is content, not register, and it is the
About page; the design record's §3.6 test is met by the chrome and the
front door, not by editing the mission. Left as is.

---

## 4. Get Involved — `support.html`

**Carried.** The whole page is a volatile content slot (D0 seam F; its own
header comment records six reframes in a week and two more since); V2 lays
nothing out that depends on its wording. Copy `[LIVE — carried unchanged]`:
the H1 *Help Us Open the Door a Little Wider* and its paragraph; What It
Actually Costs; What We're Doing About It (three bold-led paragraphs); Why
It's Worth It; Be Part of It, the fine print ("…a Colorado Public Benefit
Corporation — not a nonprofit. Contributions are not tax-deductible."), the
two Stripe buttons, the email line, the "other ways" paragraph.

**What V2 changes:** the chrome; the `.fine-print` dark fix folds into the
single dark register (no per-page override); the two give buttons take the
V2 button (madder fill, vellum text, 1.5px edge; dark edge `#E08C74`; hover
madder-deep — the live `.btn.primary:hover` goes to gold-leaf, which the
constitution's madder-as-action rule retires). Two filled buttons on this
page is the page's own action and is not the homepage's one-control rule;
the seeker's voice outranks the donor's *on the homepage* (§1.7).

RECOMMENDED: the footer line unifies to the entity line (§S.3). The header
comment block stays in the file (it is the page's own decision record).

**States:** global. **Screen reader:** H1 → four H2 sections → two buttons
("Keeping the Door Open — give once", "Open the Door Wider — give monthly";
the em-dash halves stay inside the link text) → the mailto → contentinfo.
**Responsive:** buttons wrap to a column under ~600px; nothing else diverges.

---

## 5. What's Next — `whats-next.html`

**Carried, with the pending correction as a precondition.** The live page
lists Cappadocian as "in development"; it shipped as the seventh live
tradition (PR #73). The correction is done in a worktree and not yet pushed
(Decision-Log 2026-09-02). V2's page assumes it has landed:

| # | Section | Copy | Register |
|---|---|---|---|
| 5a | Representative Modes | carried | `[LIVE — carried unchanged]` |
| 5b | More Traditions — H2 | Two new traditions are in development | `[DRAFT COPY — pending Mark's approval]` (the pending fix's wording, if different, governs) |
| 5c | More Traditions — list | Latin Pastoral-Congregational Christianity — Carthage & Hippo Regius — Cyprian, and Augustine's own congregation · Donatism — A rival North African tradition shaped by martyr-memory | `[LIVE — carried unchanged]` (Cappadocian's row removed) |
| 5d | More Traditions — paragraph | Each fills in a major, distinct strand of the ancient church not yet represented — ordinary settled parish life, and a persecuted rival tradition. Each gets the same full build as the seven traditions already live: its own representative voice, sourced vocabulary, and story material, built from its own letters, sermons, and sources. | `[DRAFT COPY — pending Mark's approval]` (the live sentence with the third strand and "six" removed) |
| 5e | Reformation Era · Atlas Upgrade · Academic Review · User Access | carried | `[LIVE — carried unchanged]` |

**Two content checks for Mark (⚠ — rulings 37 and 38 in the design
record's register, so the freeze pass sees them):** the page's meta
description still says "three new worlds" — the tradition-not-world rule and
the count both apply (ruling 37); and the Atlas Upgrade section says Church
in History "currently covers the traditions Church in Conversation has built
or plans to build," while the Atlas that shipped 2026-08-03 maps all 292
census entries across ten eras (and `support.html` says so). One of the two
pages is stale; D3 does not know which sentence Mark wants (ruling 38).

**States:** global. **Screen reader:** H1 "Where we're headed" → six
sections, the traditions as a list with bold names and muted meta →
contentinfo. **Responsive:** single column.

---

## 6. Privacy — `privacy.html`

**Carried** `[LIVE — carried unchanged]`: What's stored · Who reads it ·
Retention · Deletion · Questions. The live page describes the *conversation*
(saved and cataloged on the project's side; reviewed by the team; deletion
by email). V2 adds one section for what the *website* now does:

| # | Copy | Register |
|---|---|---|
| 6a | Eyebrow: On this website · H2: A question you type on the home page stays with you | `[DRAFT COPY — pending Mark's approval]` |
| 6b | If you write a question on the home page, it is held in your browser only. It is kept in the page's address after the `#` sign — the part of an address a browser never sends to any server, ours included — so that you can come back to it, share it, or bookmark it. Nothing is stored by us and nothing is sent anywhere until you press Send inside a conversation. | `[DRAFT COPY — pending Mark's approval]` |
| 6c | If you follow a link into a conversation, this site remembers on your own device that you have been here before, so it can offer you a quicker way in next time. That is a single setting stored in your browser; it is never sent to us and you can clear it with your browser's site data. | `[DRAFT COPY — pending Mark's approval]` (ruling 12) |
| 6d | A conversation itself is not saved to an account — it lives in the browser tab you open it in. What we keep on our side is described above. | `[DRAFT COPY — pending Mark's approval]` |

The live header uses an `<img>` of the mark here (the only page that does);
the V2 chrome replaces it. **States:** global. **Screen reader:** H1 "What we
do with a conversation" → six sections → two mailto links → contentinfo.

---

## 7. Pilot Feedback — `pilot-feedback.html`

**Carried unchanged in substance** `[LIVE — carried unchanged]`: the H1
*Tell us what you found*, the lede, the opt-in note, the seven questions with
their hints, the name and email fields, the submit, the mailto fallback
sentence, the long-answer copy box.

**What V2 changes:** the chrome; the form takes the V2 controls (44px inputs,
1.5px graphite borders, madder focus ring; the submit is the V2 filled
button); the `.optin` gold-leaf left rule stays (a rule); the three dark-mode
overrides fold into the single register; the footer takes the standard four
links. RECOMMENDED, in service of ruling 9's open audience question: add one
hint to the "confusing" prompt — *(for example: anything on a tradition's
page that read as a test you had to pass)* `[DRAFT COPY — pending Mark's
approval]` — so the Creed-note question is asked of the people it concerns.

**States:** *Default* — the form. *Submit with JavaScript* — a `mailto:` link
is built from the fields and opened; the visitor sends it from their own
mail client. *Long answers (> ~1,800 characters of link)* — the copy-and-paste
box appears, focused and selected, with its instruction. *No JavaScript* —
the form's own `action="mailto:"` POST fallback (unreliable in some
browsers, as the page's own comment records; strictly better than nothing).
*Error* — none the site can detect; the fallback sentence covers "nothing
opened."

**Screen reader:** H1 → the note → form: seven labelled fields (each label
carries its hint), select, two optional identity fields, button "Send this
to us", the fallback paragraph → [the copy box, labelled] → contentinfo.
**Keyboard:** chrome → select → input → 5 textareas → 2 inputs → submit →
mailto links → footer. **Responsive:** single column; textareas full width.

---

## 8. Church in History — `atlas-v3.html` (its own track)

**Not rebuilt here.** The Atlas runs its own palette and header today (D0
seam C); the 02 defense's twelve-item rework brief (design record §11.2) is
the plan for it, executed as a separate build track with its own rulings for
Mark (the portrait rule; the Creed note's placement; the audience question).
What V2 fixes about the Atlas is only what touches it from outside: the nav
label "Map" and the page title "Church in History" are both kept; the
homepage links to it once by that name; when the rework lands, the Atlas
adopts the V2 chrome (§S) so the wordmark and nav are the same on every page.
The redirect stubs `atlas.html` and `world-atlas.html` are unchanged.

**No "Tour" entry point** is added anywhere (D0 seam E); `tour.html` stays
unlinked and unchanged.

---

## 9. 404 — `404.html` (new, RECOMMENDED)

Cloudflare Pages serves a root `404.html` when present; today there is none.
One short page in the V2 chrome:

| # | Copy | Register |
|---|---|---|
| 9a | H1: There's nothing at this address. | `[DRAFT COPY — pending Mark's approval]` |
| 9b | The door is still open. Start with your question on the home page, or go straight to a conversation. | `[DRAFT COPY — pending Mark's approval]` |
| 9c | Links: Home · Go straight to a conversation → (the app) | labels `[LIVE]` / `[DRAFT COPY — pending Mark's approval]` |

No mark on this page (its sentence is not owed where the mark is absent).
Title, description and `noindex` in S.6. **States:** global. **Screen
reader:** H1, one paragraph, two links.

---

## Appendix A — Draft-copy index (every line awaiting Mark's approval)

Each line here is `[DRAFT COPY — pending Mark's approval]`; approving a line
means approving its words as they stand. Verbatim, live, census, record,
canon, starters, capture and brief material is not listed — it is not
drafted, and its own gates are in the design record: rulings 2, 3, 4, 20,
and **36 for the arranged brief material**, which reaches Mark's approval
pass through that ruling, tradition by tradition, not through this list.


**Shared chrome**
- S.2 Been here before? Go straight to a conversation → · S.3 (footer line unification — no new words; ruling 39)
- S.6 The tradition-page description pattern: {Name} is an AI voice for {the tradition, as its tile names it}, {dates}. Where the record is quiet, the questions people bring, and what {she/he} is built from. · Chloe's instance: Chloe is an AI voice for the house-churches of Antioch, Asia Minor and Rome, 70–200 CE. Where the record is quiet, the questions people bring, and what she is built from.
- S.6 404 title: Nothing at this address — Church in Conversation · 404 description: There's nothing at this address. The door is still open — start with your question on the home page.

**Home**
- 1.1d Welcome back. Go straight to a conversation →
- 1.2 Removed 2026-09-03 — see §1.2 above.
- 1.3c Who would you like to have a conversation with?
- 1.3d Christian traditions from the Church's first four centuries, each with one voice that speaks for it from its own letters and records. Ask any of them.
- 1.3d′ You will be in conversation with a representative voice, not a person who lived — built from one tradition's own letters and records, and honest about where they run out.
- 1.3h Her/His record → (— {Tradition})
- 1.3i′/j′ This is a pilot. We're listening for what people coming from four directions find here — the curious, pastors and teachers, scholars, and anyone re-examining their faith. Every conversation costs real money to run, so for now we ask each person to keep to about five. We can't enforce that; we can only ask.
- 1.3k Moved to §1.6 (the Table portal) 2026-09-03 — see below.
- 1.4 / 1.5 Removed 2026-09-03 — see §1.4/1.5 above.
- 1.6b Twenty centuries on one map · 1.6e Open Church in History →
- 1.6d More traditions are chosen and being built all the time. Christian movements across the Church's whole history are on record in the project's map — hover for a glimpse, click for depth.
- 1.6g The Table · 1.6h Set your own table
- 1.6i Bring two or three of them to one table. No one seated there is the host — you're one of the four chairs. · 1.6j Set your own table →
- 1.6k What's next →
- 1.7a Support (hidden heading)

**Tradition page (Chloe's and Theon's instances; the pattern for seven)**
- Status line: Open for conversation — you can sit down with this tradition now.
- AI line: {Name} is a representative voice for this tradition, not a person who lived — built from its own letters and records, and honest about where they run out.
- Seat line: {Name} is seated. Begin when you're ready — or read on. · Begin a conversation with {Name} · Bring {Name} to the Table →
- Who is speaking: A representative voice, speaking for a whole people — one short paragraph naming the tradition's own voices, plus the distress line.
- Where we are quiet: one short honest-limit statement, quoted, in the tradition's own words.
- Questions people bring to this table: Start with the hard one — three or four questions, each with a one-line source note.
- The Table: Come and join us at the Table · {Name} is seated. The chair beside {him/her} has been pulled out the whole time. · The other six chairs →

**What's Next**
- 5b Two new traditions are in development
- 5d Each fills in a major, distinct strand of the ancient church not yet represented — ordinary settled parish life, and a persecuted rival tradition. Each gets the same full build as the seven traditions already live: its own representative voice, sourced vocabulary, and story material, built from its own letters, sermons, and sources.

**Privacy**
- 6a On this website · A question you type on the home page stays with you
- 6b If you write a question on the home page, it is held in your browser only. It is kept in the page's address after the `#` sign — the part of an address a browser never sends to any server, ours included — so that you can come back to it, share it, or bookmark it. Nothing is stored by us and nothing is sent anywhere until you press Send inside a conversation.
- 6c If you follow a link into a conversation, this site remembers on your own device that you have been here before, so it can offer you a quicker way in next time. That is a single setting stored in your browser; it is never sent to us and you can clear it with your browser's site data.
- 6d A conversation itself is not saved to an account — it lives in the browser tab you open it in. What we keep on our side is described above.

**Pilot Feedback**
- §7 (for example: anything on a tradition's page that read as a test you had to pass)

**404**
- 9a There's nothing at this address. · 9b The door is still open. Start with your question on the home page, or go straight to a conversation. · 9c Go straight to a conversation →

---

## Appendix B — Measurements referenced in this storyboard

**Historical snapshot — predates the tradition-page short-template
rebuild and both of the 2026-09-03 homepage cuts.** The "Tradition"
column below describes the old long-form template (16,683px tall);
today's seven built tradition pages run about 270 lines and nowhere
near that height. Kept for what it documents about the measurement
method, not as a current reference — see the Decision-Log for
current, verified figures on what's actually shipped.

From the design record's §12 (converged scratch copies, Chromium
`chromium-1194`, fallback faces, the sandbox note stripped):

| Measure | Home | Tradition |
|---|---|---|
| Horizontal overflow, 320–1440, light and dark | 0 | 0 |
| Rendered text nodes checked (light / dark) | 175 / 175 | 266–267 / 266–267 |
| Minimum contrast (light / dark) | 5.37 / 5.66 | 5.39 / 5.66 |
| Contrast failures | 0 | 0 |
| Smallest text | 13px | 13px |
| Animations / transitions | 2 animated elements, 3 animation-names (the mark) / 0 | 0 / 0 |
| Under reduced motion | 0 | 0 |
| Tab stops | 40 (41 returning) in the end state; **34 (35) at launch**, ruling 4 | 32 (33 returning) |
| Header height, first-time visitor | 163px at 320–390 · 114 at 414–480 · 65 at 640 · 73 from 700 | the same chrome in the build (the hybrid's tradition file measures 169 at ≤480) |
| Page height at 390×844 | 9,441px (with the note) | 16,683px (note stripped, with the AI line) |
| Input in the first screen | 320×844 · 390×660/740/844 · 414×896 · 1280 · 1440×790 | — |
| Landmarks at 390 | AI line 807 · first offered question 1,005 · first "Ask" after a hold 770 below the landing | AI line 1,268 · seat line 1,368 · first app link 1,443 · silences 2,402 · questions 5,971 · record 9,279 · closing 16,046 |

The tradition column is re-measured at the fix pass with the AI line in
place, the side door gated and the sandbox note stripped, as this caption
says; the first issue's tradition figures (1,348 · 2,383 · 5,952 · 9,260 ·
16,027 · 16,663) had been taken with the note present, 75px on that page at
390 (design record §12).

*— D3 storyboard, 2026-09-02; fix pass the same day, after the Opus review.
Every copy line carries its register; every drafted line is in Appendix A
for Mark's approval; every number was measured on a scratch render — and
re-measured where the review found a slip — and nothing outside this file
and the design record was written.*
