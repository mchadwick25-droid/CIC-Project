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
├── The door → the seven chairs → the app (interview)  ·  Set your own table → the app (Table field)
├── traditions/<census-id>.html  ×7  (one template; Chloe's page is the reference)
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
| Tradition ×7 | {Tradition} — Church in Conversation *(Chloe's: The House-Churches — Church in Conversation)* | Pattern: {Name} is an AI voice for {the tradition, as its tile names it}, {dates}. Where the record is quiet, the questions people bring, and what {she/he} is built from. *Chloe's instance:* Chloe is an AI voice for the house-churches of Antioch, Asia Minor and Rome, 70–200 CE. Where the record is quiet, the questions people bring, and what she is built from. | title `[CENSUS — verbatim]` + the live suffix; description `[DRAFT COPY — pending Mark's approval]` — the pattern here, one instance drafted with each page as it clears ruling 4. The AI question is raised in the description itself, first, before anything else it says |
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
| 1.2g | The AI line — before any conversation link; graphite left rule, ink text | You will be in conversation with an AI system — a voice built from one tradition's own letters and records. It shows its sources as it speaks, and it will tell you where its record runs out. | `[DRAFT COPY — pending Mark's approval]` |
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

### 1.3 Who would you like to ask — `#who`

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
| 1.3c | H2 | Who would you like to ask? | `[DRAFT COPY — pending Mark's approval]` |
| 1.3d | Scope line (carries the sentence the hero gave up) | Seven Christian traditions from the Church's first four centuries, each with one voice that speaks for it from its own letters and records. Ask any of them. You can bring the same question to more than one. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3e | Era heading, H3 (×2) | The Early Church Era · 70–312 CE / The Imperial Church Era · 312–451 CE | `[CENSUS — verbatim]` (the census's era heads carry hyphens; the dash seam is a data fix — design record §11.3) |
| 1.3f | Seven chairs (see the table below) — each an `<li>`: 72px portrait in a 2px tint ring (56px ≤480) · H4 name with the role beside it in muted sans · tradition name in italic · dates · region in sans · the tile · two text actions | — | `[CENSUS — verbatim]` |
| 1.3g | Chair action 1 (bold sans text link, current-colour underline, 44px) | Ask {Name} → | `[DRAFT COPY — pending Mark's approval]` (pattern) |
| 1.3h | Chair action 2 (muted text link) | Her/His record → *(visually hidden: " — {Tradition}")* | `[DRAFT COPY — pending Mark's approval]` (pattern) — present only when that tradition's page exists (ruling 4). **At launch that is Chloe's chair alone**: the other six chairs carry one action, "Ask {Name} →", and nothing in the second slot — no placeholder, no "coming soon," no disabled link (§1.8, the launch row; the review's R1) |
| 1.3i | Pilot note — **below the seven**, the live site's own order | This is a pilot. We're intentionally looking for a limited number of participants across four perspectives — general, pastor or teacher, academic, and anyone re-examining their faith. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3j | Cost caveat — below the seven | Because of cost, we're asking each participant to keep to about five conversations for now — we can't enforce this yet, only ask. | `[LIVE — carried unchanged]` — **ruling 20 ⚠** |
| 1.3i′/j′ | **Offered re-draft for ruling 20** (replaces 1.3i–j if Mark takes it) | This is a pilot. We're listening for what people coming from four directions find here — the curious, pastors and teachers, scholars, and anyone re-examining their faith. Every conversation costs real money to run, so for now we ask each person to keep to about five. We can't enforce that; we can only ask. | `[DRAFT COPY — pending Mark's approval]` |
| 1.3k | The second door | Or bring two or three of them to one table. Set your own table → | `[DRAFT COPY — pending Mark's approval]` — the link is `?mode=table`, the app's empty Table field, which is what the copy says (ruling 11). Whether a free entry point surfaces the Table at all is **ruling 35** (D0's seam G, the once-planned paid tier); if the gate stands, this line is cut and nothing else moves |

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
question · Edit it · Who's at the table · Who would you like to ask? · scope
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
| **Launch state** (ruling 4 — the most likely shipping configuration; the review's R1) | Only Chloe's tradition page exists. Her chair carries two actions; the other six carry "Ask {Name} →" alone, the tile and every census field unchanged, the second slot simply absent — nothing greyed, nothing promised. The chairs list is asymmetric and says so to a screen reader by having one link where the others have two; no other line on the page changes. A tradition's record link appears the day its page clears. Measured on a scratch copy in this state: **34 tab stops** for a first-time visitor (35 returning), against 40 in the end state (§1.9). |
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
"Who would you like to ask?" → scope → H3 era → list of 3: each H4 "{Name}
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

## 2. Tradition page — the template (reference: Chloe, `tradition-chloe.html`)

**Purpose.** One tradition, one voice, one chair — reached one click deep
from a chair on the homepage or from a held question. Let the voice say who
is speaking and where its record is quiet before it offers the record; then
the record, whole; then the chair, filled.

**URL.** RECOMMENDED `traditions/<census-id>.html` — the census id joins the
homepage chair, the app deep link and (via `world_id`) the record store.
Build choice; `tradition-<short>.html` is acceptable if Mark prefers flat
files.

**H-level outline:** H1 tradition name → H2 *An AI system, speaking for a
whole people* → H2 *What this record cannot tell you — said first* (H3 ×5
silences) → H2 *Start with the hard one* → H2 *The hardest true thing about
us* → H2 *What she is built from…* (H3 ×8) → H2 *Come and join us at the
Table*. No skipped levels (verified). No mark, no motion on this page.

**Content sources — every section maps to a field, never to invented prose:**

| Section | Source |
|---|---|
| Identity line, H1, formal name, tile | census: era title · `dates` · `region`; `entry.worldName`; `name`; `entry.tile` |
| Status line | census `statusWord` ("Open for conversation") rendered into one sentence (draft) |
| Portrait and caption | `assets/portraits/<file>`; caption from that portrait's own research trail (In-App-Icons-Graphics thread), drafted per tradition |
| Who is speaking | `records/<prefix>/voice_craft/*.craft.<rep>-voice` — the `identity` field and the guard line, quoted with the record id |
| Where we are quiet | `records/<prefix>/honest_limit/*` — the participant-facing statement of each, in the tradition's "we" voice, with a source note beside each (draft) |
| Questions people bring | P-cell canon questions that map to the tradition's records, with the record source under each (draft); the tradition's own starter draft's hard openers when cleared (ruling 3) |
| In {her/his} own words | two `records/<prefix>/doctrinal_witness/*` texts, with the lexicon live on the tradition's Tier-1 `records/<prefix>/term/*` (plain meaning = the term record's own; fuller entry drafted from its sources) |
| The record behind the voice | census `longDescription` · `voices` · `sourcing` · `floorNote` · `legacy` · `experienceToday`; the tradition's reviewer's brief in `Ministry/Scholarly-Review/` (sources table, gravities, contested ground, the four press questions), arranged — ruling 36; four traditions have one, three do not |
| Review status | drafted; no counts, no dates; "a reviewer's brief is on file" only where one is |

**The seven instances — what the record store holds today (2026-09-02):**

| Tradition (census id) | Record prefix / `world_id` | honest_limit | doctrinal_witness | term | voice_craft | Status |
|---|---|---|---|---|---|---|
| The House-Churches (`post-apostolic-house-church`) | `pahc` / same | 4 | 17 | 13 | 1 | all 156 records `status: draft` — reference page built |
| Alexandrian Christianity (`alexandria-catechetical`) | `alx` / same | 3 | 13 | 51 | 1 | all 192 draft |
| Syriac Christianity (`syriac-edessa-nisibis`) | `syr` / same | 4 | 22 | 10 | 1 | all 183 draft |
| Church and Empire (`imperial-juridical-christianity`) | `ijc` / `imperial-juridical` (id seam) | 7 | 12 | 12 | 1 | all 182 draft |
| Desert Fathers and Mothers (`desert-monasticism`) | `desert` / same | 6 | 16 | 18 | 1 | all 190 draft |
| The Cappadocian Churches (`cappadocian-nicene-pastoral-monastic-tradition`) | `cappadocian` / `cappadocian-trinitarian` (id seam) | 2 | 26 | 39 | 1 | all 259 draft |
| The Bethlehem Circle (`hieronymian-ascetic-literary`) | `hal` / same | 4 | 16 | 23 | 1 | all 173 draft |

Every tradition has the census and record fields the template draws on.
Every record is in draft — ruling 4 gates all seven pages. A page ships only
when its quoted records clear; until then the homepage chair carries no
record link (§1.8, the launch row).

**Reviewer's brief on file (ruling 36; the review's R7):** the
House-Churches — `CiC_World1_Brief_for_Reviewers_Source.md`; Desert Fathers
and Mothers — `CiC_WorldBrief_Desert_V0_1_DRAFT.md`; the Bethlehem Circle —
`CiC_WorldBrief_Hieronymian_V0_1_DRAFT.md`; Syriac Christianity —
`CiC_WorldBrief_Syriac_V0_1_DRAFT.md`. **None** for Alexandrian
Christianity, the Cappadocian Churches or Church and Empire (their
Facilitation Briefs, where they exist, are a different artifact — written
for the Facilitator, not for reviewers, and not what §2.8 arranges). On a
page whose tradition has no brief, §2.8e's table, §2.8f, §2.8h's contested
list and §2.8k's four questions are absent — not paraphrased from the build
documents — until a brief exists and clears (§2.10).

The silences do not generalise evenly: 2 `honest_limit` records
(Cappadocian) to 7 (Church and Empire), plus the guard line — three
sections to eight against Chloe's five. The template's rule is the same at
every count: whole, said first, no accordion; the page length moves with it
(design record §9).

### 2.1 Breadcrumb, title block, portrait

| # | Element | Copy (Chloe's instance) | Register |
|---|---|---|---|
| 2.1a | Breadcrumb `<nav>` | Home › Who's at the table › The House-Churches | labels `[LIVE]` / `[CENSUS]` |
| 2.1b | Identity line (sans, uppercase, muted) | The Early Church Era · 70–200 CE · Antioch, Asia Minor, Rome | `[CENSUS — verbatim]` |
| 2.1c | H1 | The House-Churches | `[CENSUS — verbatim]` |
| 2.1d | Formal name, italic muted | Post-Apostolic House-Church Christianity | `[CENSUS — verbatim]` |
| 2.1e | Status line, 3px tint left rule | Open for conversation — you can sit down with this tradition now. | `[DRAFT COPY — pending Mark's approval]` — drafted from `statusWord` only where it reads "Open for conversation" (six of seven). The Cappadocian entry carries `"Built & Live"` and `glyph: "live"` (a census seam, design record §11.3; the review's r9); Chilo's page never renders it — the sentence above is the one status line, and the census is where the fix goes |
| 2.1f | Tile | The house-churches of Antioch, Asia Minor, and Rome, 70 to 200 CE — the scattered gatherings that held together after the apostles were gone, connected by letters, formed around the table, still discerning who should lead and what the body's suffering truly means. | `[CENSUS — verbatim]` |
| 2.1g | Portrait plate (4:5 crop, hairline border, max 20rem; the figure never dimmed) | alt: Chloe: a woman in a veil drawn up over her head and a rose-colored tunic, holding a plain cup in both hands, painted against a warm neutral ground. | `[DRAFT COPY — pending Mark's approval]` |
| 2.1h | Caption | **Chloe, Household Leader.** The voice of this tradition — a painted portrait, not a photograph: a face from this tradition, not one person. The veil, the plain wool, and the shared cup are grounded in the tradition's own sources; her complexion is an inference from where she lived, and is labeled so. | `[DRAFT COPY — pending Mark's approval]` |

### 2.2 The seat line — the chair offered once, outlined

Not sticky. First the AI line — one sentence, before either way in — then a
hairline-ruled row: a sentence, an outlined button, a quiet text link.

| # | Copy | Register |
|---|---|---|
| 2.2a | **The AI line, first** (added at the fix pass — the review's R5; the rows below were a–c): Chloe is an AI system — one voice built from this tradition's own letters and records. She shows her sources as she speaks, and she will tell you where the record runs out. | `[DRAFT COPY — pending Mark's approval]` — sans, graphite left rule, ink text: the homepage's 1.2g pattern. A paragraph, not a heading and not a tab stop. A visitor who arrives here directly — a shared link, a search result, which is what seven indexed pages are for — has passed no disclosure; this is the Brand Guidelines' "Always" and the design record's §3.7 item 8 kept on this page. Measured 1,268–1,352 at 390×844; the first app link at 1,443, after it |
| 2.2b | Chloe is seated. Begin when you're ready — or read on. | `[DRAFT COPY — pending Mark's approval]` |
| 2.2c | Begin a conversation with Chloe | `[DRAFT COPY — pending Mark's approval]` — `?worlds=<id>&mode=interview` (+ `#q=` once it lands) |
| 2.2d | Bring Chloe to a Table → *(with the landing state said — ruling 18)*: Bring Chloe to a Table — she'll be seated there; choose at least one more voice. | `[DRAFT COPY — pending Mark's approval]` — stands on ruling 35 (whether a free entry point surfaces the Table at all); cut, with its twin in §2.9d, if the gate stands |

**Arriving with a held question (RECOMMENDED):** if the URL carries `#q=…`
(the visitor came from the homepage's held state), the held block (1.3a's
grammar) renders above the seat line — beneath the AI line — and both chair
links carry the fragment the day the app reads it — the constitution's R0
"visible through every routing state," extended one page. The fragment is
read under the design record's §5.1 rule (decode in `try/catch`, trim, 280
characters, `textContent` only — the review's R6) on this page exactly as
on the homepage.

### 2.3 On this page — RECOMMENDED (ruling 22)

A short `<nav aria-label="On this page">` of five in-page links under the
seat line — *Who is speaking · Where we are quiet · Questions people bring ·
In her own words · The record* — so a twenty-screen phone page is navigable
without an accordion. `[DRAFT COPY — pending Mark's approval]` for the five
labels (they mirror the section eyebrows). Build note (the review's r15):
these are fragment links, so a plain click would replace a held `#q=` and a
share taken afterwards would lose the question; with JavaScript they scroll
by script and leave the hash alone (design record §11.6), and without it
no question was ever held.

### 2.4 Who is speaking

| # | Copy | Register |
|---|---|---|
| 2.4a | Eyebrow: Who is speaking · H2: An AI system, speaking for a whole people | `[DRAFT COPY — pending Mark's approval]` |
| 2.4b | Chloe is a voice, not a person who lived, and she never pretends otherwise. She is this tradition's own surviving witnesses — Ignatius, Polycarp, Clement of Rome, Hermas, Justin, the Didache — given one voice, and she speaks the way a people speaks of itself: *we*, *our*, *among us*. Where those witnesses disagreed, she keeps the disagreement visible rather than settling it for them. Her name and her role are the only invented things about her; every claim she makes belongs to the record, and she will tell you plainly when the record runs out. | `[DRAFT COPY — pending Mark's approval]` |
| 2.4c | Sidenote: **Source.** The voice's own identity record, `pahc.craft.chloe-voice`: "her name and role are the only sanctioned fabrications this build allows; every quote and claim behind them belongs to this [tradition's] own surviving voices." | quotation `[RECORD — verbatim, status: draft in the store]` with the bracketed elision (ruling 17); the framing `[DRAFT COPY — pending Mark's approval]` |
| 2.4d | If a conversation touches real distress, a separate, clearly-labeled voice steps in to direct you toward real human support. | `[LIVE — carried unchanged]` — once per page |

### 2.5 Where we are quiet — said first

| # | Copy | Register |
|---|---|---|
| 2.5a | Eyebrow: Where we are quiet · H2: What this record cannot tell you — said first | `[DRAFT COPY — pending Mark's approval]` |
| 2.5b | Epigraph, italic: Where the historical record is thin, we let the silence stand. | `[VERBATIM — locked, Brand Guidelines]` — once per page |
| 2.5c | In Chloe's own voice, from the tradition's own record. These are the silences the voice carries into every conversation. | `[DRAFT COPY — pending Mark's approval]` |
| 2.5d | Five silences, each an H3 + the record's participant-facing statement, whole (ruling 22): **The enslaved among us** (145 words, `pahc.limit.enslaved-voices`) · **Women's own words** (140, `pahc.limit.womens-own-words`) · **The quiet majority** (134, `pahc.limit.ordinary-majority`) · **The rooms themselves** (163, `pahc.limit.material-remains` — with "a later [tradition]" elided, ruling 17) · **One voice, under guard** — the `guard` field of `pahc.craft.chloe-voice`, **102 words, quoted from its second sentence to its end (91 words)**. Its first sentence, *"The one fleet floor line, absolutely: honest thinness over invented depth,"* is the build's instruction to itself, not the voice speaking, and would trip the Never list's jargon rule; it is cut, and the cut is declared here and on the page (2.5e) — the review's R4, under ruling 17's own precedent | H3s `[DRAFT COPY — pending Mark's approval]`; the four `honest_limit` statements `[RECORD — verbatim, status: draft in the store]` (ruling 4); the fifth `[RECORD — from its second sentence, the opening sentence elided and declared; status: draft in the store]` |
| 2.5e | A source sidenote beside each — e.g. **Source.** Pliny, *Letters* 10.96 — the two enslaved women called *ministrae*, examined under torture: the only place an enslaved member of this tradition comes individually into view, and through an interrogator's pen. Record: `pahc.limit.enslaved-voices`. — and, beside the fifth: **Source.** The voice's own guard line, `pahc.craft.chloe-voice`, from its second sentence; the first is the build's instruction to itself, not the voice. | `[DRAFT COPY — pending Mark's approval]` (×5) |

The margin apparatus appears only where a record stands behind the sentence
(01's narrowed rule). Sidenotes sit inside the paragraph after the sentence
they source (correct reading order), float into a 17rem margin at ≥1100px,
and set as indented notes in flow below that.

### 2.6 Questions people bring to this table

| # | Copy | Register |
|---|---|---|
| 2.6a | Eyebrow: Questions people bring to this table · H2: Start with the hard one | `[DRAFT COPY — pending Mark's approval]` |
| 2.6b | These are doors, not a syllabus. You are never confined to them, and a question none of them anticipated meets Chloe on the same terms. Each opens a conversation with her; you ask it yourself in the room — for now, nothing is sent ahead. Under each, where her record can answer from. | `[DRAFT COPY — pending Mark's approval]` (the "for now" clause is deleted when `#q=` lands) |
| 2.6c | Seven questions, the personal first, the historian's last — each a 44px link into the interview, with a visually hidden " — ask Chloe": 1 · I grew up being told doubt was sin. Was there room among your people for doubt? · 2 · I pray and nothing happens. Did your people know that silence? · 3 · The church that raised me protected people who caused harm. Your churches had failures too — what did you do with them? · 4 · You've told me what women's days were like — but could a woman carry real authority among you, and what did it cost her? | `[CANON — verbatim, canon_status: seed]` (ruling 2) |
| 2.6d | 5 · The clearest outside account of what your worship actually looked like came from torturing two enslaved women. Doesn't that taint everything we think we know from it? · 6 · If one of your churches has a bishop and another doesn't even recognize that office, how can you honestly call yourselves the same church? · 7 · Isn't "we're still arguing about it" just a nicer way of saying you don't actually know? | `[STARTERS — verbatim, W1 draft]` (ruling 3 — pending; the list ships with four until cleared) |
| 2.6e | Under each, the source line — e.g. Hermas, *Mandate* 9 — doubt named as a condition to work against, not a disqualification. · Pliny, *Letters* 10.96 (the *ministrae*); Hermas, *Vision* 2.4 (Grapte) — and the silence named above. | `[DRAFT COPY — pending Mark's approval]` (×7) |

Per tradition, the four canon questions are chosen by which of the 23 P-cell
questions the tradition's own records can answer from (ruling 13's option B
is this mapping, done here first). The hybrid's visible provenance note
("Both await Mark's review before print") does not ship; the tags above do
that work.

### 2.7 In her own words — the lexicon grammar, live

| # | Copy | Register |
|---|---|---|
| 2.7a | Eyebrow: In her own words · H2: The hardest true thing about us | `[DRAFT COPY — pending Mark's approval]` |
| 2.7b | What Chloe says when asked what her people never settled, and whether there was room for doubt — from the record, as the voice carries it. The dotted words open the tradition's own lexicon: hover or focus for the plain meaning, click or tap through for the full entry. | `[DRAFT COPY — pending Mark's approval]` |
| 2.7c | Two witness texts: *If you want the hardest true thing about us, it is this: we never agreed on who should lead…* (184 words, `pahc.witness.what-we-never-settled`, confidence Widely Accepted) · *One of us, Hermas, was told plainly: put doubting away from yourself…* (106 words, `pahc.witness.doubt-and-asking`, confidence Documented) — both counts are the record's `text` field alone (the first issue gave 297 for the first, the rendered count with its four lexicon glosses; the review's r3) | `[RECORD — verbatim, status: draft in the store]` |
| 2.7d | Four lexicon terms inside the first text — *episkopos · presbyteros · diakonos · presbyterion* — each a `<button>` with a Tyrian dotted underline, described by its gloss | the plain meanings `[RECORD — verbatim]` (`pahc.term.*`); the fuller Level-3 entries `[DRAFT COPY — pending Mark's approval]` (×4), each ending with its sources |
| 2.7e | Source sidenotes beside each text — e.g. **Source.** Hermas, *Mandate* 9. The record's own caution: this comes from one Roman visionary text, addressed mainly to sin and second repentance — it speaks for how this one figure was taught to answer doubt, not for every household. | `[DRAFT COPY — pending Mark's approval]` (×2) |

**The grammar** (the app's own, §2.4 of the constitution): hover or focus =
the Level-2 card (a vellum card with a Tyrian left rule: the word, the plain
meaning, a "Full entry →" control); click or Enter = Level 3, a side panel
(420px, vellum, own scroll) on desktop and a bottom sheet (≤55vh, the text
visible above) on phone; Escape or × closes and returns focus. On touch: first
tap = the card as a fixed popover above the thumb (measured 621–824 of 844),
second tap = the panel. Level 2 reaches assistive tech whether or not the
card is painted (the term's accessible description *is* the gloss —
verified). Marked the first time only. The ✲ appears on this page nowhere as
a control; it is a picture on the homepage only.

### 2.8 The record behind the voice — Direction 03's finding aid, one screen deep

| # | Sub-section | Copy | Register |
|---|---|---|---|
| 2.8a | Eyebrow + H2 | The record behind the voice · What she is built from, and how much of it can be trusted | `[DRAFT COPY — pending Mark's approval]` |
| 2.8b | Intro | Everything above is drawn from here. What follows is the record's own account of itself: what the tradition is, whose words survive, what the reconstruction rests on, where it is contested, and what a reviewer would press first. | `[DRAFT COPY — pending Mark's approval]` |
| 2.8c | H3 What this tradition is | the census `longDescription` (one paragraph) | `[CENSUS — verbatim]` |
| 2.8d | H3 Voices in the record | the census `voices` list (Ignatius · Clement · Polycarp · Justin · the unnamed householders) | `[CENSUS — verbatim]` |
| 2.8e | H3 What it rests on | The record's own one-line assessment: *Moderate; communal voice rich, individual interior voice thin (disclosed on its tile).* — then the sources table (Source · Standing · Disclosed dependency; eight rows; scrolls inside its own container on a phone) | `sourcing` `[CENSUS — verbatim]`; table `[BRIEF — arranged]` from `CiC_World1_Brief_for_Reviewers_Source.md` §"The evidentiary base" (ruling 36); the note "Standings and dependencies are this tradition's reviewer's brief's own words, arranged as a table." `[DRAFT COPY — pending Mark's approval]` |
| 2.8f | H3 What organizes it | A "gravity" is a force the evidence shows actually organizing the community's life. Each candidate was tested six ways and classed by how much of the record carries it; one did not clear the bar and is kept on record as a tested non-finding. — then the seven gravities (Primary ×2 · Supporting ×3 · Tensional · Declined) with one reason each | intro `[DRAFT COPY — pending Mark's approval]`; list `[BRIEF — arranged]` from the brief's §"What organizes the world" (ruling 36) |
| 2.8g | H3 Confidence and contested ground | Every term and story in this record carries one of five labels, strongest to weakest — the same five words you will meet inside the conversation, never adjusted for who is asking. — the five-glyph legend (Documented · Widely Accepted · Dominant Modern Reconstruction · Contested · Inferential / Thin) **beside** the contested list, never before content; the contested list (three items) | intro `[DRAFT COPY — pending Mark's approval]`; labels the constitution's own (Article 17); list `[BRIEF — arranged]` |
| 2.8h | H3 Where this record is contested, by its own account | The contested list (three items — the single-manuscript dependencies, the Ignatian authenticity dispute, the Egypt exclusion), each carrying its glyph from the legend beside it | `[BRIEF — arranged]` from the brief's §"The evidentiary base," second paragraph (ruling 36). This is the record section's sixth H3, its own heading in the reference — the first issue folded it into 2.8g and counted seven H3s against the outline's eight (the review's r2) |
| 2.8i | The floor note, last in this sub-section (ruling 9) | Where it stands on the Creed — the census's floor note · These communities lived two centuries before the Nicene Creed was written. What they confessed is part of the raw material the creed was later drawn from, not a departure from it. | label `[DRAFT COPY — pending Mark's approval]`; note `[CENSUS — verbatim]` |
| 2.8j | H3 Legacy, and where to stand today | the census `legacy` paragraph; the two `experienceToday` links (Dura-Europos; Yale University Art Gallery) | `[CENSUS — verbatim]` |
| 2.8k | H3 Review status, and where a reviewer might press first | Internal review: Each of the ten build steps was review-gated. Revision is expected, and recorded. · External academic review: Not yet begun. A reviewer's brief is on file; an advisory board to facilitate independent review is being formed and needs funding and volunteers. · Published on purpose — the four questions the record's own authors would most want a scholar of the period to test. — the four press questions · If this is your field: info@churchinconversation.com. And the live test: ask Chloe what she cannot know, and see whether she answers like a witness. | status and framing `[DRAFT COPY — pending Mark's approval]`; the four questions `[BRIEF — arranged]` from the brief's §"Where a reviewer might poke first" (ruling 36). On a page whose tradition has no brief, "A reviewer's brief is on file" and the "Published on purpose" block are omitted; the rest of the sub-section stands |

Project jargon on this surface — "gravity," "Tensional," "Declined," "tested
non-finding" — is defined inline where it appears; the review flagged it
against the Never list, and the build should keep each such word to one
defined use.

### 2.9 The closing door — the chair, filled

A centred band on vellum at the end of the page — the one centred block on a
left-aligned page, and the one place the register leans toward a summons
(the review's honest observation); kept at the least exposed placement, and
named here for Mark to look at.

| # | Copy | Register |
|---|---|---|
| 2.9a | Eyebrow: The Table | `[DRAFT COPY — pending Mark's approval]` |
| 2.9b | H2: Come and join us at the Table | `[VERBATIM — locked, Brand Guidelines]` (once on this page; nowhere on the homepage) |
| 2.9c | You have read what Chloe is built from, where it is thin, and what she will not claim. The chair has been pulled out the whole time. | `[DRAFT COPY — pending Mark's approval]` |
| 2.9d | Begin a conversation with Chloe (filled) · Bring Chloe to a Table — she'll be seated there; choose at least one more voice (outlined; ruling 18) | `[DRAFT COPY — pending Mark's approval]` |
| 2.9e | Because of cost, we're asking each participant to keep to about five conversations for now — we can't enforce this yet, only ask. | `[LIVE — carried unchanged]` — ruling 20 governs this line here too |
| 2.9f | The other six chairs → (to `index.html#who`) | `[DRAFT COPY — pending Mark's approval]` |

### 2.10 States

| State | What the visitor sees |
|---|---|
| **Default** | The page as above; the AI line at 1,268px (390×844, note stripped), the chair outlined at the top (1,368px), filled at the end (16,046px). |
| **Tradition without a reviewer's brief** (ruling 36 — Alexandria, the Cappadocian Churches, Church and Empire today) | §2.8e's table, §2.8f, §2.8h and §2.8k's four questions are absent; the census-derived sub-sections (2.8c, d, the `sourcing` line, 2.8i, 2.8j) and the review-status lines stand, minus "A reviewer's brief is on file." The record section reads shorter and says less; it does not paraphrase the build documents to fill the gap. |
| **Arrived with a held question** | The held block above the seat line (RECOMMENDED, §2.2); the chair links carry `#q=` once the app reads it. |
| **Lexicon — hover/focus** | The Level-2 card beside the term (fixed popover above the thumb below 1100px); `aria-expanded="true"`; the term stays expanded while focus is anywhere inside its wrapper. |
| **Lexicon — Level 3** | The panel (side, or bottom sheet ≤640) with the word, the plain meaning, the fuller entry, the sources; focus on ×; Escape/× returns focus to the term; the text is never covered on desktop and stays visible above the sheet on phone. |
| **Touch** | First tap the card, second tap the panel (verified). |
| **No JavaScript** | Every section present; the term is a button whose description is the gloss; the card shows on hover/focus by CSS; the Level-3 panel is unavailable and the card's "Full entry" control is not rendered (the build hides it without script rather than showing a dead control). |
| **Dark** | §6.2; the tradition's ring and rule in its `colorDark`. |
| **Reduced motion** | Nothing moves on this page in any state. |
| **Print** | Every section; the seat line, actions, panel and header hidden; sidenotes in flow. |
| **Record not yet cleared (ruling 4)** | The page does not exist; the homepage chair shows no record link. No placeholder. |

### 2.11 Accessibility behaviour

**Screen reader, top to bottom:** skip link → banner → main → navigation
"Breadcrumb" (Home › Who's at the table › current) → the identity line → H1
→ formal name → status → tile → complementary "Portrait": image (alt),
caption → the AI line, read as a paragraph (2.2a) → region "Chloe is
seated": sentence, link "Begin a conversation with Chloe", link "Bring Chloe
to a Table…" → [navigation "On this page"] →
H2 "An AI system…" → paragraph with an inline note (Source…) → the distress
line → H2 "What this record cannot tell you — said first" → the epigraph →
list of 5: H3, statement, note → H2 "Start with the hard one" → intro → list
of 7 links "…— ask Chloe", each followed by its source line → H2 "The hardest
true thing about us" → intro → paragraph containing 4 buttons ("episkopos",
expanded/collapsed, described by the gloss) → second paragraph → notes → H2
"What she is built from…" → 8 H3 sub-sections, the table with a caption and
scoped headers, the gravities list, the legend, the contested list, the floor
note, legacy, two external links, the status list, four press questions, the
mailto → H2 "Come and join us at the Table" → sentence → two links → the cost
line → link "The other six chairs" → contentinfo. The closed Level-3 panel is
`visibility:hidden` and absent from the tree.

**Keyboard (32 stops for a first-time visitor; 33 returning, the side door
after the nav — a real Tab walk on the fix-pass copy):** skip → wordmark →
nav → 2 breadcrumb links (Home, Who's at the table; the current page is
text, not a link — the first issue counted three, and its 33 was the
hybrid's ungated side door) → Begin → Bring → [5 on-this-page links] → 7
question links → 4 lexicon buttons (Tab moves term to term; Enter opens
Level 3; the card's "Full entry" is `tabindex="-1"` by design — pointer and
touch only) → 2 external links → the mailto → Begin → Bring → the other six
chairs → 4 footer links. Inside the panel: × (focused on open) → back to the
term on Escape/×.

**Touch:** every padded control ≥44px. The lexicon buttons and the
breadcrumb links **must** carry a 44px hit area (design record R-A4; the
constitution's §2.4) — the reference measures the four terms at 29px tall
(74×29, 86×29, 67×29, 92×29) and the breadcrumb links at 34px, so this is a
build fix the verifier checks, not a property of the reference (the
review's r1). The two external links and the mailto are inline prose links.

### 2.12 Responsive behaviour

| Width | Behaviour |
|---|---|
| ≥1100 | Reading column 38rem with a 17rem reserved margin; sidenotes float right and clear; the Level-2 card anchored beside the term. |
| 900–1099 | Title block two columns (text 7fr, portrait 4fr); sidenotes in flow, indented; the card a fixed popover. |
| 640–899 | Single column; portrait plate under the title block, max 20rem. |
| <640 | Header wraps; sources table scrolls inside its own container; gravities stack to one column; status grid one column; Level-3 = bottom sheet (12px top radius, ≤55vh); seat line wraps; the page is 16,683px at 390×844 with the AI line (about twenty screens; sandbox note stripped) — the cost of carrying the silences whole (ruling 22), navigable by §2.3, whose five-link nav is not in that figure (it adds one short row). |
| 320 | Overflow 0 (verified). |

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

One note for the copy pass rather than a rule (the review's r16): a few
drafted lines stack two negations in one sentence — 2.1h ("a painted
portrait, not a photograph: a face from this tradition, not one person"),
2.4b ("a voice, not a person who lived"). The Never list bans stacked "not
X, it's Y" as a sentence shape; the Always list keeps "a clarifying contrast
naming what kind of thing this is," which is what these are. Defensible;
Mark's eye is the test.

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
- 1.2g You will be in conversation with an AI system — a voice built from one tradition's own letters and records. It shows its sources as it speaks, and it will tell you where its record runs out.
- 1.2h Or begin with one of these — questions people bring
- 1.2j These are from the project's own set of questions, the same set every voice is prepared to meet. Any of them, or your own, is asked in the room.
- 1.3a Edit it · 1.3c Who would you like to ask?
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

**Tradition page (Chloe's instance; the pattern for seven)**
- 2.1e Open for conversation — you can sit down with this tradition now.
- 2.1g (alt) Chloe: a woman in a veil drawn up over her head and a rose-colored tunic, holding a plain cup in both hands, painted against a warm neutral ground.
- 2.1h Chloe, Household Leader. The voice of this tradition — a painted portrait, not a photograph: a face from this tradition, not one person. The veil, the plain wool, and the shared cup are grounded in the tradition's own sources; her complexion is an inference from where she lived, and is labeled so.
- 2.2a Chloe is an AI system — one voice built from this tradition's own letters and records. She shows her sources as she speaks, and she will tell you where the record runs out.
- 2.2b Chloe is seated. Begin when you're ready — or read on. · 2.2c Begin a conversation with Chloe · 2.2d Bring Chloe to a Table — she'll be seated there; choose at least one more voice.
- 2.3 Who is speaking · Where we are quiet · Questions people bring · In her own words · The record
- 2.4a Who is speaking · An AI system, speaking for a whole people
- 2.4b Chloe is a voice, not a person who lived, and she never pretends otherwise. She is this tradition's own surviving witnesses — Ignatius, Polycarp, Clement of Rome, Hermas, Justin, the Didache — given one voice, and she speaks the way a people speaks of itself: we, our, among us. Where those witnesses disagreed, she keeps the disagreement visible rather than settling it for them. Her name and her role are the only invented things about her; every claim she makes belongs to the record, and she will tell you plainly when the record runs out.
- 2.4c (framing of the source note)
- 2.5a Where we are quiet · What this record cannot tell you — said first
- 2.5c In Chloe's own voice, from the tradition's own record. These are the silences the voice carries into every conversation.
- 2.5d The five H3s: The enslaved among us · Women's own words · The quiet majority · The rooms themselves · One voice, under guard
- 2.5e The five source notes (as in the reference implementation), the fifth now reading: Source. The voice's own guard line, `pahc.craft.chloe-voice`, from its second sentence; the first is the build's instruction to itself, not the voice.
- 2.6a Questions people bring to this table · Start with the hard one
- 2.6b These are doors, not a syllabus. You are never confined to them, and a question none of them anticipated meets Chloe on the same terms. Each opens a conversation with her; you ask it yourself in the room — for now, nothing is sent ahead. Under each, where her record can answer from.
- 2.6e The seven source lines (as in the reference implementation)
- 2.7a In her own words · The hardest true thing about us
- 2.7b What Chloe says when asked what her people never settled, and whether there was room for doubt — from the record, as the voice carries it. The dotted words open the tradition's own lexicon: hover or focus for the plain meaning, click or tap through for the full entry.
- 2.7d The four fuller lexicon entries (episkopos · presbyteros · presbyterion · diakonos), as in the reference implementation
- 2.7e The two source notes
- 2.8a The record behind the voice · What she is built from, and how much of it can be trusted
- 2.8b Everything above is drawn from here. What follows is the record's own account of itself: what the tradition is, whose words survive, what the reconstruction rests on, where it is contested, and what a reviewer would press first.
- 2.8e Standings and dependencies are this tradition's reviewer's brief's own words, arranged as a table.
- 2.8f A "gravity" is a force the evidence shows actually organizing the community's life. Each candidate was tested six ways and classed by how much of the record carries it; one did not clear the bar and is kept on record as a tested non-finding.
- 2.8g Every term and story in this record carries one of five labels, strongest to weakest — the same five words you will meet inside the conversation, never adjusted for who is asking.
- 2.8i Where it stands on the Creed — the census's floor note (label)
- 2.8k Internal review: Each of the ten build steps was review-gated. Revision is expected, and recorded. · External academic review: Not yet begun. A reviewer's brief is on file; an advisory board to facilitate independent review is being formed and needs funding and volunteers. · Published on purpose — the four questions the record's own authors would most want a scholar of the period to test. · If this is your field: info@churchinconversation.com. And the live test: ask Chloe what she cannot know, and see whether she answers like a witness.
- 2.9a The Table · 2.9c You have read what Chloe is built from, where it is thin, and what she will not claim. The chair has been pulled out the whole time. · 2.9d (the two actions) · 2.9f The other six chairs →

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
