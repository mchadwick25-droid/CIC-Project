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
  brief for outside reviewers in `Ministry/Scholarly-Review/`, arranged as a
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
├── The door → the seven chairs → the app (interview)  ·  Set your own table → table.html (NEW, change order 2026-09-03)
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
the page's first control (homepage: the question input — verified).

### S.2 Header

**Anatomy, left to right, wrapping:** the wordmark **Church *in* Conversation**
(a link to Home; `[VERBATIM — locked, Brand Guidelines]` — Alegreya 700, the
*in* italic 400, no "The"); the site nav, five text links; for a returning
visitor only, the side door.

| Element | Copy | Register |
|---|---|---|
| Wordmark | Church *in* Conversation | `[VERBATIM — locked, Brand Guidelines]` |
| Nav | Home · About · What's Next · Map · Get Involved | `[LIVE — carried unchanged]` |
| Side door (returning visitors only) | Been here before? Go straight in → | `[DRAFT COPY — pending Mark's approval]` |
| Side door, ≤640px | Go straight in → | (the long half hidden) |

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
"Site": five links (+ "Been here before? Go straight in" when returning).
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
| Home | Church in Conversation: The First Centuries | Twenty centuries of the Church's story, one era at a time. Seven Christian traditions you can sit down with today, from the Early Church and Imperial Church eras. Come and join us at the Table. | `[LIVE — carried unchanged]` — the description as corrected by the pending "six → seven" push (design record §11.4) |
| Tradition ×7 | {Tradition} — Church in Conversation *(Chloe's: The House-Churches — Church in Conversation)* | Pattern: {Name} is a representative voice for {the tradition, as its tile names it}, {dates}. Where the record is quiet, the questions people bring, and what {she/he} is built from. *Chloe's instance:* Chloe is a representative voice for the house-churches of Antioch, Asia Minor and Rome, 70–200 CE. Where the record is quiet, the questions people bring, and what she is built from. *Theon's instance:* Theon is a representative voice for the school and church of Alexandria, c. 150 to 400 CE. Where the record is quiet, the questions people bring, and what he is built from. | title `[CENSUS — verbatim]` + the live suffix; description `[DRAFT COPY — pending Mark's approval]` — the pattern here, one instance drafted with each page as it clears ruling 4. 2026-09-03 change order: "an AI voice" → "a representative voice," matching the fleet-wide wording fix (design record §3.7 item 8) |
| About · Get Involved · Privacy · Pilot Feedback · Church in History (and its two redirect stubs) | live | live | `[LIVE — carried unchanged]` |
| What's Next | What's Next — Church in Conversation | ⚠ the live description says "three new worlds in development" — **ruling 37** | title `[LIVE]`; description is Mark's |
| 404 | Nothing at this address — Church in Conversation | There's nothing at this address. The door is still open — start with your question on the home page. — plus `<meta name="robots" content="noindex">`, since Cloudflare Pages serves the page with a 404 status and it should never be indexed | `[DRAFT COPY — pending Mark's approval]` (both) |

---

## 1. Home — `index.html`

**Purpose.** Take what the visitor brought. Open with the hook; then who can
carry it, so a question can be asked with real context instead of into a
void; then one real place to put that question down; then what a
conversation is like; then what holds it to the record and what is
unfinished; then the map; then the ask.

**Change order, 2026-09-02 (Decision-Log): §1.2 and §1.3 swap order —
Mark's ruling.** A visitor handed a bare "ask a question" box before seeing
who is even there has no way to know what's askable or trustworthy; the
seven need to be met first, so the question that follows is "I want to ask
*her* something, because I trust she has the context to answer it," not a
generic prompt into empty air. §1.3's own content, mechanism and register
tags are unchanged by the swap — only its position, and the door's, move.
§1.3's chairs are also regrouped as a gallery (rows = era, columns =
chronological order within the era) rather than a single stacked list, so
the section stays scannable as more traditions and eras are added — see the
new §1.3 below. **§1.8's state table, §1.9's accessibility walk-through and
keyboard-path counts, and §1.10 below are written to the *pre-swap* order
and have not yet been re-verified against the new one** — re-verify before
they're relied on for anything beyond the general shape of each state.

**Order of the page (H-level outline):** H1 hook → §1.3 H2 *Who would you
like to ask?* (H3 era ×2, H4 name ×7) → §1.2 H2 *Start with your question* →
§1.4 H2 *What a conversation looks like* (H3 ×4 margin notes) → §1.5 H2 the
disclosure (H3 ×2) → §1.6 H2 *Church in History* → §1.7 H2 *Support*
(visually hidden). No skipped levels (verified against the build).

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
| 1.1d | Welcome-back line (returning visitors only; hidden otherwise) | Welcome back. Go straight in → | `[DRAFT COPY — pending Mark's approval]` |

The first text on the page is the mark's sentence — the Logo Usage Sheet's
caption rule discharged, an explicit choice (ruling 8). Centred; the H1 at
`clamp(2rem, 4.5vw, 3rem)`, weight 500.

### 1.2 The door

The page's first surface and its only filled control. A vellum box with a
hairline border; inside it, top to bottom:

| # | Element | Copy | Register |
|---|---|---|---|
| 1.2a | H2 (also the input's accessible name) | Start with your question | `[VERBATIM — constitution]` |
| 1.2b | Visually hidden `<label for="q">` | Your question | `[DRAFT COPY — pending Mark's approval]` |
| 1.2c | Text input, `maxlength` 280, 44px tall, 1.5px graphite border, ground-coloured | — | — |
| 1.2d | The control — an in-page link styled as the one filled button (madder fill, vellum text; in dark the 1.5px `#E08C74` edge carries the boundary) | Choose who to ask → | `[DRAFT COPY — pending Mark's approval]` |
| 1.2e | The lede (names the person Mark named, in the first screen) | Whether you come curious, with a sermon to write, or with a question about faith you've carried for years — there is a chair. | `[DRAFT COPY — pending Mark's approval]` |
| 1.2f | The "how" line — **interim wording, until `#q=` lands in the app** | Write it in your own words. It stays in this browser tab and is sent to no one until you press Send in the room — for now, you will type it again there. | `[DRAFT COPY — pending Mark's approval]` |
| 1.2f′ | The "how" line — **the day `#q=` lands** (replaces 1.2f) | Write it in your own words. It stays in this browser tab and is sent to no one until you press Send in the room — where it will be waiting for you. | `[DRAFT COPY — pending Mark's approval]` |
| 1.2g | The AI line — before any conversation link; graphite left rule, ink text | You will be in conversation with a representative voice, not a person who lived — built from one tradition's own letters and records, and honest about where they run out. | `[DRAFT COPY — pending Mark's approval]` — 2026-09-03 change order (Mark): drop the "AI system" / program-explanation framing everywhere it leads a page; lead with the world and the tradition, not the mechanism. A brief "representative voice" statement carries the substance of item 8's disclosure without the system-explanation register |
| 1.2h | Offered-questions heading (uppercase, letterspaced sans label, muted — never small caps, ruling 19) | Or begin with one of these — questions people bring | `[DRAFT COPY — pending Mark's approval]` |
| 1.2i | Six offered questions, each a 44px link, italic, a madder dash before and arrow after | 1 · I grew up being told doubt was sin. Was there room among your people for doubt? · 2 · Did any of you ever want to leave? · 3 · I pray and nothing happens. Did your people know that silence? · 4 · The people who taught me the faith turned out to be hypocrites. Did that happen among you? · 5 · Why does God allow suffering like this? Where was he when it happened to your people — and to mine? · 6 · I want to believe in Jesus, but I can't. What would you say to me? | `[CANON — verbatim, canon_status: seed]` (rulings 2, 10, 13) |
| 1.2j | Note under the list | These are from the project's own set of questions, the same set every voice is prepared to meet. Any of them, or your own, is asked in the room. | `[DRAFT COPY — pending Mark's approval]` — the hybrid's visible "seed-status" tag does not ship |

**Behaviour** (design record §5.1): with JavaScript, the control and Enter
hold the question; each offered question holds its text; the URL's fragment
becomes `#q=…`; the page scrolls to §1.3 and focus moves to the held block.
Without JavaScript, the control is a plain jump to `#who`; the input keeps
its text; nothing is held or written to the URL. There is no `<form>` and no
query string anywhere (ruling 30).

**Measured:** input at 456–504px on 390×844/740/660, 537–585 at 320×844,
455–503 at 1280 and 1440×790 — in the first screen everywhere; the lede fully
in screen one from 740, its first line visible at 660; the AI line at 807
(390), before the first offered question at 1,005; zero app links precede
the AI line for a first-time visitor (verified).

### 1.3 Who would you like to have a conversation with — `#who`

**Now the first screen after the hero (2026-09-02 change order above), not
the door's landing zone — context before the ask.** Top to bottom:

**The chairs are a gallery, not a stacked list (2026-09-02 change order):**
each era heading is followed by a grid, `repeat(auto-fill, minmax(150px,1fr))`,
so an era's chairs run left to right in chronological order and the next
era starts a new row below — vertical position reads as time, horizontal
position within a row reads as chronology within that era. This is the
scale answer for "more than ten": a new tradition joins its era's row
(wrapping to a second row under the same era heading if the row is full)
rather than lengthening a single column everyone has to scroll past.
Portrait, name, role, tradition, dates, and both chair actions (§1.3g/h)
are unchanged; the descriptive tile sentence (§1.3f's `entry.tile`) is
still full census-verbatim text in the DOM, `-webkit-line-clamp: 2` for
sighted layout only — a screen reader still hears the whole sentence.

**The gallery shows every era that fits, in full — never a partial one
(2026-09-02/03, three change orders the same conversation: cap both
eras together, narrow to one row, then back to "as many whole eras as
fit," which is where it settled):** each era (heading + chairs) is its
own `.era-group`, `scroll-snap-align: start`. A `sizeGallery()` pass
sums each group's real rendered height against a per-tier target
(800px ≥700px, 1380px 481–699px, 1560px ≤480px — the same numbers as
the first, both-eras change order, since that's still what today's
content needs) and sets the container's `max-height` to the exact sum
of whichever whole eras fit — never mid-era, recomputed from live
content rather than hand-measured, so it stays correct as content
changes. Those per-tier numbers are also the CSS fallback for no-JS,
and happen to already show both of today's eras with no scrollbar on
their own. A `← Previous era / {Era} · N–M of T / Next era →` control
appears **only when content actually overflows**
(`scrollHeight > clientHeight` — with today's two eras, never); Next
and Previous each compute the best-fitting page in their direction
(not just ±1 era), and focus follows so the move is announced. Without
JavaScript the gallery is a plain scrollable region (`tabindex=0`),
every era and name in static markup, reachable by wheel, touch, or
keyboard — the nav control simply never appears. **The last-visible
era needs dynamically-computed trailing padding to reach the
container's top when scrolled to** (nothing follows it otherwise, so
the browser clamps the scroll short — confirmed directly, twice, in two
different shapes of this feature); that padding is computed fresh each
time against whichever era is currently last, not hand-measured, so it
stays correct regardless of how many eras exist. `[hidden]` on
`.era-nav` needed its own `{display:none}` rule to actually take effect
— the same specificity bug the design record's §11.6 already named for
`.site-nav a[hidden]`, worth checking for on any future element that is
both given a `hidden` attribute and its own `display` in CSS.

| # | Element | Copy | Register |
|---|---|---|---|
| 1.3a | The held block (hidden until a question is held): a vellum block with a 3px lapis left rule; `tabindex="-1"`, `aria-labelledby` the label and the question | Your question, held: · *the visitor's own words, italic* · Edit it | `[VERBATIM — constitution]` for the label; "Edit it" `[DRAFT COPY — pending Mark's approval]` |
| 1.3b | Eyebrow | Who's at the table | `[LIVE — carried unchanged]` |
| 1.3c | H2 | Who would you like to have a conversation with? | `[DRAFT COPY — pending Mark's approval]` — 2026-09-03 change order (Mark): the project's name is *Church in Conversation*; a question is how one starts, but the conversation is the point, and the heading should say so |
| 1.3d | Scope line (carries the sentence the hero gave up) | Seven Christian traditions from the Church's first four centuries, each with one voice that speaks for it from its own letters and records. Ask any of them. You can bring the same question to more than one. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3e | Era heading, H3 (×2) | The Early Church Era · 70–312 CE / The Imperial Church Era · 312–451 CE | `[CENSUS — verbatim]` (the census's era heads carry hyphens; the dash seam is a data fix — design record §11.3) |
| 1.3f | Seven chairs (see the table below) — each an `<li>`: 72px portrait in a 2px tint ring (56px ≤480) · H4 name with the role beside it in muted sans · tradition name in italic · dates · region in sans · the tile · two text actions | — | `[CENSUS — verbatim]` |
| 1.3g | Chair action 1 (bold sans text link, current-colour underline, 44px) | Ask {Name} → | `[DRAFT COPY — pending Mark's approval]` (pattern) |
| 1.3h | Chair action 2 (muted text link) | Her/His record → *(visually hidden: " — {Tradition}")* | `[DRAFT COPY — pending Mark's approval]` (pattern) — present only when that tradition's page exists (ruling 4). **As of D4 Increment 3 (2026-09-03), that is Chloe's and Theon's chairs**: the remaining five chairs carry one action, "Ask {Name} →", and nothing in the second slot — no placeholder, no "coming soon," no disabled link (§1.8, the launch row; the review's R1) |
| 1.3i | Pilot note — **below the seven**, the live site's own order | This is a pilot. We're intentionally looking for a limited number of participants across four perspectives — general, pastor or teacher, academic, and anyone re-examining their faith. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3j | Cost caveat — below the seven | Because of cost, we're asking each participant to keep to about five conversations for now — we can't enforce this yet, only ask. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3i′/j′ | **Offered re-draft for ruling 20** (replaces 1.3i–j if Mark takes it) | This is a pilot. We're listening for what people coming from four directions find here — the curious, pastors and teachers, scholars, and anyone re-examining their faith. Every conversation costs real money to run, so for now we ask each person to keep to about five. We can't enforce that; we can only ask. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3k | The second door — the link now carries a small copy of the Arriving mark (§1.2's own SVG, `id="table-cue"`), playing its draw-and-settle motion once, the first time the line scrolls into view (`IntersectionObserver`, disconnects after firing) | Or bring two or three of them to one table. Set your own table → | `[DRAFT COPY — pending Mark's approval]` — the link is `table.html` (2026-09-03 change order: the Table became its own page, §2a), not the app directly (ruling 11's original "empty Table field" premise no longer holds — `table.html` itself hands the app that link once ≥2 seats are filled). **Ruling 35 (2026-09-03): no gate.** This line stands unconditionally |

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

**Measured after a hold (390×844):** the landing screen reads — held
question · Edit it · Who's at the table · Who would you like to have a
conversation with? · scope
· The Early Church Era · Chloe. No pilot paragraph, no cost paragraph in the
landing zone. The first "Ask Chloe" is 770px below the landing point.

### 1.4 One exchange, as it happened

| # | Element | Copy | Register |
|---|---|---|---|
| 1.4a | Eyebrow | One exchange, as it happened | `[DRAFT COPY — pending Mark's approval]` |
| 1.4b | H2 | What a conversation looks like | `[DRAFT COPY — pending Mark's approval]` |
| 1.4c | Intro | A visitor pressed Theon on how sure he really was. This is what came back — the voice holding apart what it knows from what it cannot show. | `[DRAFT COPY — pending Mark's approval]` |
| 1.4d | The leaf — a `<figure>` on vellum (ruling 21) with a hairline border, set in the app's decided long-form grammar: a running head, the Facilitator's two lines in italic muted with a graphite rule, the "You" label in lapis over the question in italic, the Representative's label in ink with a gold-leaf rule, three paragraphs of prose, dotted terms and the ✲ 3 as pictures | Running head: *Alexandrian Christianity · c. 150–400 CE* · Facilitator: *I'm glad you're here. Come in, settle wherever feels right.* / *Welcome to the table. Today you sit with Theon, a catechetical teacher from the Christian community of Alexandria, speaking to you from somewhere within the second through fourth centuries of that great city's life — a place where scripture, philosophy, and the discipline of the soul were held together in one breath. Theon awaits your questions; where shall we begin?* · You: *What's the actual evidence for how confident we can be about that practice? How sure are you, really?* · Theon · Catechetical Teacher: *We told you the shape a formation likely took, not one seeker's counted days. That is worth holding apart plainly, because the two are not equally sure.* / *The stages themselves — coming first as one still under instruction, the waiting before the water, the illumination baptism itself is named to be, the deepening afterward that never counts itself finished — these we hold with real confidence, because they are not inference. They are the pattern our own life set down and still keeps: the great fast, the feast that follows it, the daily return to a Scripture never read once and shelved. That rhythm is not reconstructed. It is what we do.* / *What we cannot give you is one particular soul walking it — a name, a morning, a specific word said to a specific catechumen on a specific day. When we spoke of "a typical formation," that was offered honestly as the shape many lives probably shared, not as any single life we can point to and say: this happened, here, to this one. Where the pattern is concerned, our confidence is real. Where a particular soul's road through it is concerned, we have the outline and not the portrait — and we would rather tell you that plainly than paint a face onto it that was never there.* ✲ 3 | `[CAPTURE — verbatim]` — the capture's obsolete "Known limitation" banner is not transcribed (it no longer exists in the app; the current disclosure is 1.5g) |
| 1.4e | Caption, dated (the review's condition, the defense's fix) | Captured from a live conversation with Theon on 25 August 2026; the words are unchanged, re-set here in the app's long-form grammar. The dotted terms and the ✲ are live in the room — hover or tap them there for the plain meaning, and for the sources. Here they are a picture. | `[DRAFT COPY — pending Mark's approval]` |
| 1.4f | Margin note 1, H3 + text | The quieter voice · The italic lines are the Facilitator, who opens the room, bridges anything the voice could not know, and — if something painful comes up — points you toward real people who can help. | `[DRAFT COPY — pending Mark's approval]` (a paraphrase; the distress line itself appears verbatim once per page, at 1.5g) |
| 1.4g | Margin note 2 | A dotted term · Opens a short gloss in the tradition's own words; one tap more opens the full entry. Marked the first time it appears, then left alone. | `[DRAFT COPY — pending Mark's approval]` |
| 1.4h | Margin note 3 | ✲ 3 · the sources · Three letters and records stand behind this answer. In the room you open the list, and every one is checkable. | `[DRAFT COPY — pending Mark's approval]` |
| 1.4i | Margin note 4 | Where it's thin · Where the historical record is thin, we let the silence stand. | H3 `[DRAFT COPY — pending Mark's approval]`; the sentence `[VERBATIM — locked, Brand Guidelines]` |

The leaf has no composer, no Send, no chrome. ≥900px: leaf and margin notes
side by side (1.35fr / .65fr); below, the notes follow the leaf.

### 1.5 Before you sit down — the disclosure block

| # | Element | Copy | Register |
|---|---|---|---|
| 1.5a | Eyebrow | Before you sit down | `[DRAFT COPY — pending Mark's approval]` |
| 1.5b | H2 | This is an AI system. Here is what holds it to the record, and what is still unfinished. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5c | Column 1, H3 | What holds it | `[DRAFT COPY — pending Mark's approval]` |
| 1.5d | Bullet | **Locked to sources.** A voice is built last, from a completed record of one tradition's own letters, sermons, and primary sources, through a ten-step, review-gated build — and speaks only from that record. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5e | Bullet | **Shows its confidence.** Every claim carries how well it is attested, in the same five words inside every conversation, never adjusted for who is asking. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5f | Bullet | **Watched while it speaks.** Every conversation is watched in real time for a softened truth, an invented detail, or knowledge the voice shouldn't have — and corrected before it reaches you. | lead `[DRAFT COPY — pending Mark's approval]`; sentence `[LIVE — carried unchanged]` (about.html) |
| 1.5g | Bullet | **Witness, never recruitment.** A voice of its tradition, in real conversation — it does not pretend to be a person, and it is not here to win you over. | `[DRAFT COPY — pending Mark's approval]` (the protected line the hybrid used here now appears once, at 1.5o) |
| 1.5h | Column 2, H3 | What is unfinished, said plainly | `[DRAFT COPY — pending Mark's approval]` |
| 1.5i | Bullet | **Independent academic review is the standard we are building toward.** It has not begun; an advisory board is being formed and needs funding and volunteers. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5j | Bullet | **Every conversation runs on one plain voice.** The modes designed for a pastor, a scholar, or someone re-examining faith have not shipped. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5k | Bullet (new — the disclosure the capture's banner stood for, in its current true form; `Conversation.tsx` 44, `sessionStore.ts`) | **Lives in one browser tab, not an account.** There is no sign-in; a conversation stays in the tab you open it in. What we keep on our side, and how to ask us to delete it, is on the Privacy page. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5l | Bullet | **Later centuries are planned, not built.** What is live is the Church's own first four hundred years; each later era is its own careful build. | `[DRAFT COPY — pending Mark's approval]` |
| 1.5m | Bullet | If a conversation touches real distress, a separate, clearly-labeled voice steps in to direct you toward real human support. | `[LIVE — carried unchanged]` (about.html) — once per page |
| 1.5n | Closing line, italic | We are committed to representing each Christian movement in full — its testimony, beautiful and hard alike. | `[VERBATIM — locked, Brand Guidelines]` |
| 1.5o | Closing line, muted | We measure whether each Christian movement is represented in an engaging and accurate way. What it means for you is yours to own and share. | `[VERBATIM — locked, Brand Guidelines]` |
| 1.5p | Link line | How a tradition is built, step by step: About — how it works. | `[DRAFT COPY — pending Mark's approval]` (links `about.html#how-it-works`) |

No counts, no dates, no status numbers (a status number is a maintenance
promise). Each project negative is said once, here, and nowhere above the
fold of any page. ≥760px two columns; below, stacked.

### 1.6 Church in History — one link

| # | Element | Copy | Register |
|---|---|---|---|
| 1.6a | Eyebrow | Twenty centuries on one map | `[DRAFT COPY — pending Mark's approval]` |
| 1.6b | H2 | Church in History | `[LIVE — carried unchanged]` (the Atlas's own name) |
| 1.6c | Paragraph | Seven traditions are open for conversation and two more are chosen and being built. Nearly three hundred movements across ten eras are on record in the project's map — hover for a glimpse, click for depth — so that what is not yet built is still there to be read. | `[DRAFT COPY — pending Mark's approval]` — "nearly three hundred" is the live site's own wording for the census's 292; "two more" is the census's `Selected - Not Yet Built` count |
| 1.6d | Links | Open Church in History → · What's next | `[DRAFT COPY — pending Mark's approval]` |

No map band (ruling 23). Consistent with the Atlas rework track.

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
| **First visit** | No side door, no welcome-back line. Hook, door, six questions; the AI line before any conversation link. |
| **Returning** (flag set) | The side door in the header; *Welcome back. Go straight in →* under the hook. Everything else identical — the seven never move, never in a carousel. |
| **Launch state** (ruling 4 — the most likely shipping configuration; the review's R1) | As of D4 Increment 3 (2026-09-03), Chloe's and Theon's tradition pages exist. Their chairs carry two actions; the remaining five carry "Ask {Name} →" alone, the tile and every census field unchanged, the second slot simply absent — nothing greyed, nothing promised. The chairs list is asymmetric and says so to a screen reader by having two links on some chairs and one on others; no other line on the page changes. A tradition's record link appears the day its page clears. The single-page-state measurement below (34/35 tab stops) predates this increment and needs remeasuring against the current two-page state; not yet redone. |
| **Question held — typed** | Submit (control or Enter): the held block renders at the top of §1.3 with the question; URL `#q=…`; scroll to §1.3; focus on the held block; next Tab → *Edit it*. |
| **Question held — offered** | Tapping an offered question: the same, with that text; the input is filled with it too. |
| **Question held — restored** | Arriving at a URL carrying `#q=…` (shared, bookmarked, Back from the app): the held block is shown without scrolling; the input carries the text. |
| **Edit it** | Focus returns to the input, scrolled to centre; re-submitting replaces the held text. |
| **Empty submit** | Scroll to §1.3, nothing held, focus on the section. |
| **No JavaScript** | Control and offered questions jump to `#who`; the input keeps its text; no hold, no URL. Every name and app link present (7 names, 10 app links). |
| **Dark** | §6.2 dark table; the button's boundary is its `#E08C74` edge; the tints are the `colorDark` values (rings only). |
| **Reduced motion** | The mark still, seated; nothing else moves in any state. |
| **Print** | Header, support slot, skip link hidden; every section present. |
| **After `#q=` lands in the app** | Each "Ask {Name}" href carries `#q=<the held question>`; 1.2f′ replaces 1.2f. Same-tab hand-off (ruling 15): Back returns to this page with the question restored. |

### 1.9 Accessibility behaviour

**What a screen reader encounters, top to bottom:** skip link → banner:
"Church in Conversation" link, navigation "Site" (5 links) → main → H1 (the
hook) — the mark is decorative and silent; its sentence is read as a
paragraph before the H1 → H2 "Start with your question" → edit text
"Start with your question" (named by the H2) → link "Choose who to ask" →
the lede → the "how" line → the AI line → the list heading → list of 6 links
(each the full question) → the note → [after a hold: the held block, focused,
announced as "Your question, held: {question}", then link "Edit it"] → H2
"Who would you like to have a conversation with?" → scope → H3 era → list of 3: each H4 "{Name}
{Role}", tradition, dates and region, the tile, link "Ask {Name}", link
"{Her/His} record — {Tradition}" (at launch, only Chloe's item has the
second link; the other six end at "Ask {Name}") → H3 era → list of 4 → the
pilot note, the cost caveat → "Or bring two or three of them to one table." link "Set your
own table" → H2 "What a conversation looks like" → figure (labelled by its
caption): the leaf read as prose, "✲ 3" with `aria-label` "three sources
cited" → complementary "How to read the exchange": four H3 + paragraphs → H2
the disclosure → two H3 lists → the two protected lines → the About link →
H2 "Church in History" → paragraph → two links → H2 "Support" (visually
hidden) → three lines with three links → contentinfo: the entity line, four
links.

**Keyboard path (end state: 40 stops for a first-time visitor, 41
returning; launch state: 34 and 35 — both measured by a real Tab walk):**
skip link → wordmark → 5 nav links (→ side door) → [welcome-back link] →
question input → Choose who to ask → 6 offered questions → [after a hold:
Edit it] → 7 × (Ask {Name}, {Her/His} record) — at launch, Ask Chloe, Her
record, then six × Ask {Name} alone → Set your own table → About — how it
works → Open Church in History → What's next → give once → give monthly →
Get Involved → 4 footer links. Focus ring 2px madder, 3px offset. No
positive `tabindex`; nothing hidden is a stop; nothing is sticky, so the
focused element is never obscured.

**Touch.** Every control ≥44px tall: the input, the button, the six question
links, the chair actions (fourteen in the end state, eight at launch), the
Table link, the map links, the support links, the footer links, the nav. Inline prose links (the About link, the
protected lines' surroundings) ride the inline exception.

### 1.10 Responsive behaviour

| Width | Behaviour |
|---|---|
| ≥900 (desktop) | Chrome at 64rem; sections at 44rem; reading at 38rem. Input and button on one row. Exchange: leaf and margin side by side. Disclosure two columns. Header one row (73px). |
| 640–899 | Single column narrows; exchange stacks below 900; disclosure two columns from 760. Input and button on one row from 768. Header one row (65px at 640, 73 from 700). |
| <640 (phone) | Header wraps — the wordmark on its own row above two nav rows at ≤390 (163px), above one at 414–480 (114px); the nav at .9rem; door box padding 1rem; button wraps under the input (input basis 11rem); portrait 72px (56px ≤480); everything single column; no horizontal scroll at 320 (verified). |
| 320 | Input 537–585; first offered question 1,201; overflow 0. |

Page height: 9,441px at 390×844 (with the sandbox note), 6,786 at 1280.

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
(same register as the homepage's 1.2g and each tradition page's own AI line) →
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
| 9b | The door is still open. Start with your question on the home page, or go straight in. | `[DRAFT COPY — pending Mark's approval]` |
| 9c | Links: Home · Go straight in → (the app) | labels `[LIVE]` / `[DRAFT COPY — pending Mark's approval]` |

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
- S.2 Been here before? Go straight in → · S.3 (footer line unification — no new words; ruling 39)
- S.6 The tradition-page description pattern: {Name} is an AI voice for {the tradition, as its tile names it}, {dates}. Where the record is quiet, the questions people bring, and what {she/he} is built from. · Chloe's instance: Chloe is an AI voice for the house-churches of Antioch, Asia Minor and Rome, 70–200 CE. Where the record is quiet, the questions people bring, and what she is built from.
- S.6 404 title: Nothing at this address — Church in Conversation · 404 description: There's nothing at this address. The door is still open — start with your question on the home page.

**Home**
- 1.1d Welcome back. Go straight in →
- 1.2b Your question (hidden label) · 1.2d Choose who to ask →
- 1.2e Whether you come curious, with a sermon to write, or with a question about faith you've carried for years — there is a chair.
- 1.2f Write it in your own words. It stays in this browser tab and is sent to no one until you press Send in the room — for now, you will type it again there.
- 1.2f′ Write it in your own words. It stays in this browser tab and is sent to no one until you press Send in the room — where it will be waiting for you.
- 1.2g You will be in conversation with a representative voice, not a person who lived — built from one tradition's own letters and records, and honest about where they run out.
- 1.2h Or begin with one of these — questions people bring
- 1.2j These are from the project's own set of questions, the same set every voice is prepared to meet. Any of them, or your own, is asked in the room.
- 1.3a Edit it · 1.3c Who would you like to have a conversation with?
- 1.3d Seven Christian traditions from the Church's first four centuries, each with one voice that speaks for it from its own letters and records. Ask any of them. You can bring the same question to more than one.
- 1.3g Ask {Name} → · 1.3h Her/His record → (— {Tradition})
- 1.3i′/j′ This is a pilot. We're listening for what people coming from four directions find here — the curious, pastors and teachers, scholars, and anyone re-examining their faith. Every conversation costs real money to run, so for now we ask each person to keep to about five. We can't enforce that; we can only ask.
- 1.3k Or bring two or three of them to one table. Set your own table →
- 1.4a One exchange, as it happened · 1.4b What a conversation looks like
- 1.4c A visitor pressed Theon on how sure he really was. This is what came back — the voice holding apart what it knows from what it cannot show.
- 1.4e Captured from a live conversation with Theon on 25 August 2026; the words are unchanged, re-set here in the app's long-form grammar. The dotted terms and the ✲ are live in the room — hover or tap them there for the plain meaning, and for the sources. Here they are a picture.
- 1.4f The quieter voice · The italic lines are the Facilitator, who opens the room, bridges anything the voice could not know, and — if something painful comes up — points you toward real people who can help.
- 1.4g A dotted term · Opens a short gloss in the tradition's own words; one tap more opens the full entry. Marked the first time it appears, then left alone.
- 1.4h ✲ 3 · the sources · Three letters and records stand behind this answer. In the room you open the list, and every one is checkable.
- 1.4i Where it's thin (heading only)
- 1.5a Before you sit down · 1.5b This is an AI system. Here is what holds it to the record, and what is still unfinished. · 1.5c What holds it · 1.5h What is unfinished, said plainly
- 1.5d Locked to sources. A voice is built last, from a completed record of one tradition's own letters, sermons, and primary sources, through a ten-step, review-gated build — and speaks only from that record.
- 1.5e Shows its confidence. Every claim carries how well it is attested, in the same five words inside every conversation, never adjusted for who is asking.
- 1.5f Watched while it speaks. (lead only)
- 1.5g Witness, never recruitment. A voice of its tradition, in real conversation — it does not pretend to be a person, and it is not here to win you over.
- 1.5i Independent academic review is the standard we are building toward. It has not begun; an advisory board is being formed and needs funding and volunteers.
- 1.5j Every conversation runs on one plain voice. The modes designed for a pastor, a scholar, or someone re-examining faith have not shipped.
- 1.5k Lives in one browser tab, not an account. There is no sign-in; a conversation stays in the tab you open it in. What we keep on our side, and how to ask us to delete it, is on the Privacy page.
- 1.5l Later centuries are planned, not built. What is live is the Church's own first four hundred years; each later era is its own careful build.
- 1.5p How a tradition is built, step by step: About — how it works.
- 1.6a Twenty centuries on one map
- 1.6c Seven traditions are open for conversation and two more are chosen and being built. Nearly three hundred movements across ten eras are on record in the project's map — hover for a glimpse, click for depth — so that what is not yet built is still there to be read.
- 1.6d Open Church in History → · What's next
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
- 9a There's nothing at this address. · 9b The door is still open. Start with your question on the home page, or go straight in. · 9c Go straight in →

---

## Appendix B — Measurements referenced in this storyboard

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
