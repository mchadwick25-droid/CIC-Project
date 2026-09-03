# Church in Conversation — Website Design V2

**Status: FROZEN — Mark, 2026-09-02 ("Freeze it"). Converged from the
defended hybrid ("The Open Door," Direction 06). Reviewed by Opus the same
day (`Sandbox/D2-struggle/D3-synthesis-review.md`: "ready to freeze with named
required fixes" — eleven, R1–R11, and sixteen non-blocking items); applied in
this revision, each named where it lands, and spot-checked against the
review's own list before the freeze. From here, changes need a change order
(`Decision-Log.md`), not quiet edits — this file and its companion storyboard
are the binding reference for D4. The register below still carries roughly
twenty ⚠ OPEN FOR MARK items — the freeze fixes this document's shape and
content as the reference, it does not itself resolve those; each is still a
real open decision, to be ruled on as D4 reaches it or sooner if Mark wants to
clear them ahead of time. Not yet built; nothing here is live.**

**What this is.** The design record for the redesigned public website
(`cic-website/`): the philosophy as converged, how it serves the four charter
goals and the two heart tensions Mark named, the complete type / colour /
motion system with its measured contrast tables, the accessibility floor and
its binding rules, what is still sacrificed, and the register of every ruling
the process accumulated — decided, recommended, or open. The page-by-page
storyboard is its companion: `CiC_Website_V2_Storyboard.md`.

**What it is built from, in order of authority.** Mark's rulings in
`Decision-Log.md` (this folder) · the Brand Guidelines Consolidated V1.0 and
the Logo Usage Sheet V1.0 (FINAL, binding) · `CiC_Full_UX_Design_V1_0.md` (the
design constitution — governs the app; this site must not contradict it, and
every stretch of it is named below as a ruling) · the defended hybrid
(`Sandbox/D1-directions/06-hybrid-open-door/`, its `README.md`,
`homepage.html`, `tradition-chloe.html`) as the reference implementation ·
its review and defense (`Sandbox/D2-struggle/06-hybrid-open-door-review.md`,
`-defense.md`) · the five D1 directions and their ten D2 files, for what was
tried and killed · the live site (`cic-website/`) and
`data/world-census.json`.

The hybrid's two mockup files stand as the reference implementation. This
document does not re-derive them; it converges them, applies every concrete
fix the review and defense already specified and verified, resolves what the
record left to D3, and puts the rest to Mark in the open.

---

## 0. Conventions used in this document and the storyboard

### 0.1 Copy registers — the draft-and-approve rule

Every piece of participant-facing copy in either document carries exactly one
of these tags. The tag travels with the line into the build.

| Tag | Meaning |
|---|---|
| `[VERBATIM — locked, Brand Guidelines]` | One of the six protected lines, or the mark's public sentence. Quoted exactly. Not a draft; not editable here. |
| `[VERBATIM — constitution]` | A string the UX constitution or its storyboard already decided (*Start with your question* · *Your question, held:*). Not a draft. |
| `[LIVE — carried unchanged]` | Copy already public on the live site, carried without edit. Already approved once; carrying it into a new position is itself noted where it matters (ruling 20). |
| `[CENSUS — verbatim]` | A field of `cic-website/data/world-census.json`, rendered as the data has it (verbatim-and-flag: seams are flagged in §11.3, never fixed on the page). |
| `[RECORD — verbatim, status: draft in the store]` | A `records/<prefix>/*` field quoted exactly. The record itself is in draft in the store — ruling 4 governs whether it may appear publicly. |
| `[CANON — verbatim, canon_status: seed]` | A `records/_fleet/canon_question/*` question, exact. Ruling 2. |
| `[STARTERS — verbatim, W1 draft]` | An opening question from `CiC_W1_Guided_Starters_V0_1_DRAFT.md`, exact. Ruling 3. |
| **`[DRAFT COPY — pending Mark's approval]`** | **Every sentence D3 (or the hybrid's author) wrote for a visitor. None of it is final until Mark approves the actual words.** |

Two rules ride with the tags. A quote's provenance clears its facts, not its
register (the 05 defense's rule, adopted by the hybrid): nothing lifted from
app code, a record, or a data file is filed as cleared for a public surface
by virtue of being verbatim. And the corpus-wide vocabulary rule holds in
every drafted line: *tradition*, never *world*.

The storyboard adds two provenance tags of its own, `[CAPTURE — verbatim]`
and `[BRIEF — arranged]`, defined in its Conventions. The brief material is
arranged from a named file per tradition and gated by ruling 36. A
`[RECORD — verbatim]` quote that begins or ends inside the field says so
where it is used, with the record cited beside it (ruling 17; the guard line,
storyboard §2.5d) — "verbatim" never covers an undeclared cut.

### 0.2 Decision markers

- **DECIDED** — ruled by Mark, dated, cited to `Decision-Log.md`.
- **RECOMMENDED** — D3's default, with its reasoning, marked as a
  recommendation. The build follows it unless Mark rules otherwise at the
  freeze.
- **⚠ OPEN FOR MARK** — not D3's to decide: a stretch of a FINAL document, a
  brand approval, a content clearance, or a decision with a real tradeoff
  outside design. Each carries D3's recommendation where one is honest to
  give.

### 0.3 Measurement caveat

Every number in this document was taken in the same headless Chromium the
D2 reviewers used (`/opt/pw-browsers/chromium-1194`, driven by Playwright)
on scratchpad copies of the hybrid's files with the specified fixes applied
(§12). Google Fonts is unreachable from the sandbox, so every render is in
fallback faces: pixel heights are font-sensitive; ratios, overflow, DOM
order, focus behaviour and semantics are not. D4 re-measures in the real
faces before anything ships (§7.3).

---

## 1. What was converged, and from what

### 1.1 The line of descent

Five D1 directions diverged (editorial / atlas-first / institutional /
quiet-liturgical / product-led). Five Opus reviews killed all five at the
whole-site level; five defenses conceded the kills and named specific
salvage. Four of the five defenses, independently, found the same missing
move: a fast, personal way to put a hard question down — the door the
constitution designed at S0 (§5.1, *Start with your question*) and no D1
direction built. Mark chose to hybridize (Decision-Log, "Mark picks Option
A"). The hybrid was synthesized with named parentage, reviewed with the same
discipline as its parents ("survives, conditionally"), and defended (nearly
every finding conceded and fixed with measurement; two contested with
evidence and won; one cross-system decision surfaced). Mark ruled on that
decision — the held question travels to the app as a URL fragment, never a
query string — and opened D3.

This document is the convergence of that hybrid *as defended*: the review's
five conditions are met by the fixes the defense specified (§12 verifies
them), and the twenty rulings the two files accumulated are resolved or put
to Mark in §10.

### 1.2 The parentage table stands — with the defense's corrections applied

The hybrid's `README.md` §2 is the parentage record: forty-odd structural
decisions, each credited to the direction, review, or defense it came from.
The review spot-checked roughly thirty rows and found the great majority
hold. This document credits that table rather than re-deriving it, and
carries the defense's corrections to it as binding on the record:

1. **The antiquarian devices are the hybrid's own call, not a concession.**
   Roman numerals, drop caps, a colophon and small caps were argued *for* by
   name by both the 01 and 03 defenses. Their exclusion here rests on the
   constitution's "nothing antiquarian," the two reviews' readings, and Mark's
   non-religious-feel ruling — and goes to Mark as ruling 19, not as an
   inherited finding.
2. **The tradition page's order departs from 01's rebuilt order in a fifth,
   now-declared way:** 01's long essay is replaced by record-backed
   statements, and the questions list comes before the voice, not after. The
   replacement is argued (§4.3 of the storyboard); the swap is a D3 choice.
3. **"The 'For the Wrestling' set with the fear question first"** — the
   tradition page front-loads the personal, which is the substance, but the
   fear question is not on the page and "four scholars and one person" is the
   01 *defense's* paraphrase of its review. The warrant is the substance, not
   the set.
4. **The pilot sentence's placement.** "Above the rows, where the live site has
   it" was wrong: the live site has it *below* the carousel. Moving it below
   the seven restores the live order and takes it out of the door's landing
   zone (§4.3; ruling 20).

Three smaller citation slips (a spliced quotation, three words dropped from
inside a quotation, two section pointers) are corrected in the storyboard
where the material is used; every quotation there is exact, marked as a
paraphrase, or carries a declared elision with the record cited beside it
(ruling 17; the guard line in storyboard §2.5d).

### 1.3 What died, and stays dead

So that nothing is reintroduced unknowingly:

- **01 (editorial):** the site-as-book spine; chronology as the *sole*
  organizing principle; the reading-time byline; numbered plates and the
  periodical dress; `mode=table` as the primary door; the ✲ jump-anchor
  (a sixth verb). *Survives:* the chapter order (provenance → silences →
  questions → door), the sidenote implementation, the "we" register, AAA
  reading conditions for long prose.
- **02 (atlas-first):** the map as homepage; any map band on the homepage
  until the Atlas is on brand tokens; the legend-as-thesis; eleven outbound
  links. *Survives:* the twelve-item `atlas-v3.html` rework brief (§11.2), the
  never-dim-a-portrait rule (§6.4), the dark-tint audit.
- **03 (institutional):** method, status dashboard, confidence scale or
  catalogue table as front-door content; sticky marginal column; "Plate,"
  "Register," lower-roman counters; any count not generated from the census.
  *Survives:* the tradition record as the *second* screen, the AI disclosure
  block, the confidence glyph set beside the content it labels, "where a
  reviewer might press first," verbatim-and-flag.
- **04 (quiet-liturgical):** the ordo, the rubric, the silences, the order
  marker, station names, "Continue when you are ready," soft scroll-snap,
  the global `transition:none !important`. *Survives:* the restraint
  discipline with its reasons attached, the pressure checklist, the seven as
  places in a list (never a carousel), the returning visitor's side door and
  welcome-back line, the motion inventory as a deliverable format.
- **05 (product-led):** the composer, the seven filled buttons, the
  chronology-first IA, "verbatim = cleared." *Survives:* the method (refusal
  table, honesty ledger, deep-link verification, per-surface contrast math),
  the real captured exchange as the product shown, one primary per screen,
  the inner-page anatomy as a template.

---

## 2. The philosophy, as converged

**The visitor is a guest who arrived with something, not a reader who
arrived curious. The site's first job is to take what they brought.**

So the homepage opens with the protected hook and, directly beneath it, one
real place to write a question — in the first screen on every shipping phone
(§12) — and six real questions people bring, each a door. The question is held
on the page in the constitution's own R0 grammar (*Your question, held:*),
editable, never discarded, never sent to anyone until the visitor presses
Send in the room; the page says so exactly. Everything else on the homepage
serves that first move or follows from it: who can carry the question (the
seven, as places, chronological, one action each); what a conversation
actually looks like (one captured exchange — a skeptic's press, answered by a
voice naming its limit); what holds the thing to the record and what is
unfinished (the disclosure block, raised by us, before any conversation
link); one link to the map; the support slot in the quietest register.

One click deep, a tradition's page says in one line that the voice is an AI
system — before either chair link, because a shared link or a search result
lands here without passing the homepage — and then lets the voice say who
is speaking and where its record is quiet *before* it offers the record itself — Direction
01's chapter order carrying Direction 03's record (collection → assembly →
trust → chair) as the second screen its own defense argued it always was.
Disclosure about the *tradition* leads; methodology about the *project* is
said once, in the disclosure block, and nowhere above a fold.

The register throughout is the constitution's own — *"a beautifully set
trade book on parchment — warm, unhurried, nothing antiquarian, nothing
tech-forward"* — held by two disciplines. Restraint: nothing moves but the
mark, once; nothing fades, lifts, or dims; one filled control per surface;
every colour has a job and a number. Measurement: no claim about contrast,
overflow, or semantics is made without a measurement, and the measurement
pass includes looking at the page.

What it is not: not a map, a book, a record, a rite, or a product grid. The
door is the spine. And the door is honest about its own limit today — until
the app reads the held question (§5.2), the visitor types it twice — because
building the door before the router is the right order, and pretending the
router exists would be the decoy control D2 killed.

---

## 3. The four charter goals, and the two heart tensions

### 3.1 Accessibility

WCAG 2.2 AA as the floor, with four criteria held higher because the D2
record showed AA is not met by inheritance (§7). Measured on the converged
copy, not asserted: no horizontal overflow at 320–1440px in either register;
zero text-contrast failures on either page in either register (minimum 5.37
light, 5.66 dark); nothing under 13px; no sticky chrome; a heading outline
that surfaces every Representative; Level 2 of the lexicon readable by
assistive tech; the held question announced to a screen-reader user the
moment it is held; the whole homepage present and navigable without
JavaScript, including every name and every app link.

### 3.2 Clear storytelling

The story is told in the order the person Mark named needs it: the hook; a
place for the question; who can carry it; what a conversation is like; what
holds it to the record and what is unfinished; the map; the ask. The brand's
four messages appear in the brand's order — the whole Church in the open (the
seven), it shows its work (the exchange, the disclosure), witness never
recruitment (the door's copy, the pressure checklist), the build is the
product (one link to About's method). Not chronology first, not a map first,
not a method first, not a rite first, not a picker first.

One correction to the hybrid's own claim, conceded in its defense and carried
here: the page is *opened* the way that person needs it. The picker beneath
the door is still chronological — because until the routing exists (or ruling
13 is made), chronology is the only ordering that does not pretend to know
the visitor's question.

### 3.3 Easy access to features — the honest step map

Measured on the converged homepage, 390×844, with the sandbox note that does
not ship stripped:

| Step | Position | Notes |
|---|---|---|
| The input | 456–504px | in the first screen on every phone height tested (660, 740, 844, 896) and at 320×844 (537–585) |
| The six offered questions | from 1,005px | the second screen |
| The AI line | 807px | before any conversation link, for a first-time visitor (verified: zero app links precede it) |
| After a question is held | landing at the held block | the first "Ask" link is 770px below the landing point — within the landing screen at 844 |
| A returning visitor | header, every page | one-tap side door; a welcome-back line under the hook |
| The record | one click | from Chloe's chair at launch — the only tradition page that exists until each tradition's records clear ruling 4; from any chair in the end state (storyboard §1.8, the launch row) |
| The Table | one quiet link | below the seven — ruling 35 (2026-09-03): no gate, kept unconditionally |
| The map | one link | its own section |

What the door does today: holds the question on this page, restores it from
a shared or bookmarked URL, and opens the conversation with the voice chosen.
What it does the day `#q=` lands in the app (§5.2): the question arrives
pre-filled in the room's composer, never auto-sent. The interim copy says the
visitor will type it again; that sentence is deleted the day the change
order lands.

### 3.4 Professional, cutting-edge design that draws people in

Cutting-edge the way 04 and 05 both argued and neither delivered: the
confidence to do less, measured. One filled control per screen; the locked
type pair carrying the whole hierarchy; colour that has a job and a number;
no motion but the mark; a page quiet because nothing on it is trying to
attract a click — and warm because the first thing on it is a question in the
visitor's own words. The one element most likely to read as period in five
years is the offered-questions list (a stack of italic prompts under an
input); it is kept because its content — real, specific, painful human
questions — is what saves it, and the build should know it is the surface to
watch.

### 3.5 Heart tension one — "engaging and trustworthy (scholar)"

Trustworthy *because* scholarly, not institutional distance. The scholarship
is underneath, one click away — the brand's own pair, which Direction 03 asked
to invert and its review refused. On the homepage the trust content is one
exchange where a voice is pressed on its confidence and answers by naming
what it cannot show. On the tradition page, the silences come before the
sources and the sources before the chair. The voice pairs run in order on
every surface: experience (the door, the chairs) → governance (the AI line at
the door; the disclosure block) → mechanism (a link to About). Nothing on the
front door is a credential.

### 3.6 Heart tension two — "not the feel of religion; my heart is the hard-questions seeker, not the academic"

Every register the reviews convicted is left behind: the illuminated codex
(01), the doctrinal vetting board (02), the divinity-school finding aid (03),
the order of service (04), the sepia chat product (05). What remains reads as
a well-set page with a question on it. The portraits are 72px rings in a
list, not plates. The captured exchange is a skeptic's question, not a
service. "Jesus" appears where a person's question names him — sixth of six
(ruling 10) — and in the footer's inherited entity line, and nowhere in the
chrome. The first six things a visitor can do on the page are ask about
doubt, leaving, unanswered prayer, hypocrisy, suffering, and not being able
to believe. The one place the register leans devotional — the tradition
page's closing band, a centred protected line at up to 2.3rem — is kept at
the least exposed placement available (end of an inner page) and named for
Mark to look at (storyboard §2.9).

The subject is religious and the site does not hide it: nine occurrences of
"doubt" on the tradition page, five silences in a communal "we," three
thousand words about bishops and martyrdom. That is content, not register.

**2026-09-03 addition (Mark, following the "AI system" change order
above):** the same discipline that trims religious performance from the
register also trims technology explanation from it. A tradition page is
about the tradition and the conversation it makes possible, not about how
the representative voice is built. §3.5's own ordering already says this —
governance (the AI line) comes briefly, once, before mechanism (a link to
About) — this addition is that ordering held to more strictly than the
first pass held it: the representative's own nature is named simply, in
passing, and the page moves on to the world. Exact wording is expected to
keep changing; this stance is what a future editing pass should hold to,
on every instance, not just the two built so far.

### 3.7 The pressure checklist — binding on every surface

Applied as a list, not felt as a mood (the 04 defense's item 2):

1. No urgency. No scarcity (ruling 20 governs the inherited pilot copy).
2. No countdown, no deadline, no "only / first."
3. No promised transformation; testimony only with real quotes.
4. No conversion push; the decline path from every surface is complete and
   graceful — Back, or scroll on; nothing re-presses.
5. One action per surface; the page's single filled control is the door's.
6. The ask below the door, in the quietest register on the page, as text
   links; the seeker's voice outranks the donor's.
7. Nothing sticky follows the visitor; nothing moves to attract a click.
8. The AI question raised by us, first, before any conversation link — on
   the homepage at the door (storyboard §1.2g); on every tradition page as
   one line above the seat line (§2.2a), because a direct arrival has passed
   nothing else (the review's R5). No exception is claimed on any surface.
   **2026-09-03 change order (Mark, ruling on the point directly):** the
   wording that had carried this — "an AI system," "shows its sources as
   it speaks" — led every page with the mechanism instead of the world
   being represented; wrong focus. The requirement itself stands and the
   line keeps its position, ahead of any conversation link, on every
   surface; its wording is now a brief "representative voice, not a
   person who lived" statement, carrying the same substance in the
   register the rest of the site uses. Applied fleet-wide: §1.2g, the
   homepage's "Before you sit down" section heading, §2.2a and §2.4a on
   both shipped tradition pages, and `table.html`'s own line.

---

## 4. Information architecture

### 4.1 The pages

| Page | File | V2 status |
|---|---|---|
| Home | `index.html` | **Rebuilt** to the hybrid's homepage, with the fixes in §12 |
| Tradition (×7) | `traditions/<census-id>.html` (RECOMMENDED path; build choice) | **New** — one template, seven instances; Chloe's is the reference (`tradition-chloe.html`) |
| About | `about.html` | Carried; header lockup fix; count already corrected to seven (pending push) |
| Get Involved | `support.html` | Carried; the cost/ask copy stays a slot (D0 seam F); dark-mode class fix carried |
| What's Next | `whats-next.html` | Carried; Cappadocian fix (pending push) is a precondition |
| Privacy | `privacy.html` | Carried; one new section on the question you type here (draft) |
| Pilot Feedback | `pilot-feedback.html` | Carried unchanged in substance |
| Church in History | `atlas-v3.html` | **Separate track** — the 02 defense's twelve-item rework brief (§11.2); V2 changes only its nav label and the one homepage link |
| Redirect stubs | `atlas.html`, `world-atlas.html` | Unchanged |
| Tour | `tour.html` | Pulled from nav since 2026-07-20; unchanged; unlinked; not a V2 surface |
| 404 | `404.html` | **New, RECOMMENDED** — the Worker's static-assets serving handles it; one paragraph and the door (storyboard §9) |

Every page's `<title>` and `<meta name="description">` — the strings a
search result or a shared link shows — are specified in the storyboard's
S.6, in the live site's own `X — Church in Conversation` form; the eight new
ones are drafted there under the draft-and-approve rule (the review's R10).

### 4.2 Chrome

**Header**, every page: the wordmark **Church *in* Conversation** (italic
*in* — the lockup rule the live header drops) at left; the nav — Home · About
· What's Next · Map · Get Involved — as text links with a madder underline on
hover/focus/current; for a returning visitor only, a quiet italic side door,
*Been here before? Go straight in →* (draft copy — storyboard S.2). The
header wraps on narrow screens; it
never clips, never hides a scroller, is never sticky. The mark is not in the
header (ruling 8). Below 640px the nav sets at .9rem with tighter gaps — the
one chrome change the first issue of §12 left unnamed; it is listed there
now. Measured, first-time visitor, sandbox note stripped: at 320–390 the
wordmark takes its own row above **two** nav rows — header **163px**; at
414–480 one nav row under the wordmark — **114px**; at 640 one row —
**65px**; from 700 one row — **73px**. Nav links measure 48px tall on phones
and 49px from 700, so the 44px target rule (R-A4) holds inside every
one-row header. (The first issue printed 110 / 61 / 41 here and in §12.
Those were the header heights *minus the sandbox note's height* — an
arithmetic slip; the note sits above the header and never changes it. The
fold figures were not affected: the input positions were note-stripped
correctly, and the review reproduced the fold conclusion with margin.)

**Footer**, every page: the live entity line, verbatim, and About · Feedback
· Privacy · Contact (ruling 39 for the line's unification).

**Skip link** first in DOM on every page; after it, the next Tab lands inside
`<main>` — on the homepage, on the question input for a first-time visitor
(verified); for a returning visitor the welcome-back link under the hook
comes first (storyboard §1.9).

### 4.3 The doors, and every app hand-off

Three doors, ranked — a deliberate departure from the constitution's
co-equal S0 for the *website only* (ruling 1). The constitution's three are
*Start with your question · Build your own table · Guided onboarding*; the
site keeps the first, gives the second a quiet third place, puts the
chronological picker in the middle rank, and drops guided onboarding
entirely — it is not built (D0 note §2.D; the hybrid's README §10), and
nothing here previews it:

1. **Start with your question** — the homepage's first surface.
2. **Choose a voice** — the seven chairs, the second screen; also every
   tradition page's seat line and closing door.
3. **Set your own table** — one quiet text link below the seven, to the app's
   Table field; never a primary; promises nothing about the experience.

Whether a free entry point should surface the Table at all was a business
question the D0 note flagged (seam G — multi-voice Tables were once a planned
paid tier) and no round answered until Mark ruled directly, 2026-09-03: no
gate. The third door and the tradition page's "Bring *Name* to a Table"
links stand unconditionally (ruling 35); the copy nowhere depended on them
either way.

Every hand-off into the app uses the app's own deep-link contract
(`cic-poc/frontend/src/App.tsx`, header comment, verified 2026-09-02):

| Link | Href | Lands on |
|---|---|---|
| Ask *Name* (homepage chair; tradition seat line and closing door) | `?worlds=<census-id>&mode=interview` (+ `#q=…` once §5.2 lands) | straight into the room |
| Set your own table (homepage) | `?mode=table` | the Table field, empty — as its copy says |
| Bring *Name* to a Table (tradition page) | `?worlds=<census-id>&mode=table` | the Table field with that one seat — and a *disabled* "Seat at least two voices" button today; ruling 18 |
| Go straight in (side door; welcome-back) | `/` | the launch screen |

The link texts in this table are the storyboard's, and every one of them is
`[DRAFT COPY — pending Mark's approval]` there; only *Start with your
question* is the constitution's own string.

The pre-ship live check the 05 review and defense both asked for stands: the
multi-voice Table is verified in the shipped frontend source, not on the
deployed engine (ruling 11).

### 4.4 The Atlas is its own track

The homepage links to Church in History once, by its own name, in a late
section, and builds no map band (ruling 23). The Atlas's rework — palette
convergence onto the brand tokens, DOM-as-document, per-stop headings, deep
links with `pushState`, all five edge types, the portrait rule, the phone
list form, Level-2 on touch, the 13px floor in the panel, opaque sticky era
heads, the Creed note last, zero outbound links — is the 02 defense's §5.1
brief, executed as a separate build track (§11.2). Nothing in V2's homepage
or storyboard contradicts that brief; the nav label "Map" and the page title
"Church in History" are both kept.

---

## 5. The question door — the protocol

### 5.1 On the page

- **One input, one control.** A text input (`maxlength` 280) whose accessible
  name is the H2 *Start with your question* (`aria-labelledby`), and a
  button-styled in-page link, *Choose who to ask →*. No `<form>`, no GET, no
  query string anywhere (RECOMMENDED — see §5.4 for why).
- **With JavaScript:** submit (click, or Enter in the input) holds the
  question — it renders at the top of the chairs section in the R0 grammar
  (*Your question, held:* / the question in italic / *Edit it*), the URL's
  fragment becomes `#q=<encoded question>` via `history.replaceState`, the
  page scrolls to the chairs, and **focus moves to the held block itself**
  (`tabindex="-1"`, labelled by the label and the question), so the first
  thing a screen reader announces is the question and the next Tab stop is
  *Edit it* (verified). Tapping an offered question does the same with that
  text. Arriving with `#q=` in the URL restores the held state. An empty
  submit scrolls to the chairs and holds nothing.
- **Without JavaScript:** the control is a plain in-page link — the page
  jumps to the chairs, the input keeps the typed text (no reload), nothing is
  held, nothing is sent, no URL is written (verified). Every name and every
  app link is static markup.
- **The fragment is data, never markup** (the review's R6). `#q=` is the one
  string in a shareable URL that anyone can write. On arrival and on every
  hold, the same four steps: read `location.hash`; `decodeURIComponent`
  inside `try/catch`; `trim()`; cut to **280 characters** — the input's own
  `maxlength`. The value is rendered only through `textContent` and the
  input's `value` — never `innerHTML`, never a selector, never an attribute.
  The invariant: **the URL is the held state, normalised.** An undecodable
  fragment (a malformed `%` sequence) holds nothing and is left as it is.
  An empty or whitespace-only value holds nothing, and the empty fragment is
  dropped from the URL. An over-long value is held truncated, the input
  carries the truncated text, and the fragment is rewritten to the 280 that
  were held. Every rewrite is `history.replaceState` — no navigation, no
  history entry — and on arrival the page never scrolls. Every "Ask *Name*"
  href gains `'#q=' + encodeURIComponent(text)` from the *held* value, never
  from the raw hash. This is the reference script's own behaviour
  (`.trim().slice(0, 280)`, `heldQ.textContent = text`), verified case by
  case at the fix pass (§12); the rule is stated here because the reference
  script is what D4 replaces. The app inherits it (§5.2).
- **The copy at the door says exactly what happens** (draft, storyboard §1.2):
  the question stays in this browser tab and is sent to no one until the
  visitor presses Send in the room — and, until §5.2 lands, that they will
  type it again there.

### 5.2 To the app — DECIDED: the fragment

Mark's ruling (Decision-Log, 2026-09-02, the last D2 item): **the held
question travels to the app as a URL fragment (`#q=`), never a query string.**
A fragment is never sent in any HTTP request — it stays in the browser — so
"sent to no one" is exact, and nothing lands in the app host's access logs.

What is decided is the mechanism. The Decision-Log is explicit that the
change order itself is not yet authorised ("the actual `App.tsx` change… is
D4's to build when this increment is scheduled, not done here"). Its
authorisation is **ruling 34, ⚠ OPEN FOR MARK**, with D3's recommendation
to schedule it with D4's first increment: "authorise this direction" and
"authorise one line in `App.tsx`" are the same decision, and the door is
unfinished without the second.

The contract, for the app-side change order (D4; its own decision to schedule,
its own deploy on Render — the site cannot close this gap alone):

1. `App.tsx` — `parseDeepLink()` reads `q` from `location.hash` (in addition to
   `worlds` and `mode` from the search string), **before** `consumeDeepLink()`
   strips the URL; `consumeDeepLink()` clears the hash as well as the search.
2. `Conversation.tsx` — passes the question down.
3. `ChatInput.tsx` — accepts an `initialMessage` prop into its state;
   **never auto-sends** (the constitution's own rule —
   `CiC_Full_UX_Storyboard_V1_0.md` §G.3 / §R: "pre-filled, editable,
   deletable, never auto-sent"); the participant presses Send. The value is
   a string, trimmed and capped at the composer's own maximum, set as the
   textarea's value — the same data-never-markup rule as §5.1.
4. Whether a question also travels into a Table (`TableRoom.tsx`) — a separate
   small decision inside the change order; RECOMMENDED no for now (the Table
   is convened, not asked).
5. A test, and a Render deploy.

Roughly fifteen lines across three or four files, no backend change, design
already approved. Site-side, the day it lands: every "Ask *Name*" href on a
page holding a question gains `#q=<encoded>`; the interim clause at the door
is deleted; the Privacy page's new section (storyboard §6) already describes
the fragment behaviour.

### 5.3 Same-tab hand-off — RECOMMENDED

Every app link opens in the same tab (ruling 15). The reason a new tab ever
seemed safer — the capture's "refreshing will lose your conversation" banner
— is gone from the source: sessions live in `sessionStorage` and rehydrate on
reload (`sessionStore.ts`, `App.tsx` 64–79), and the in-room note is now *Not
saved to an account — this conversation lives in this tab* (`Conversation.tsx`
44). Same-tab makes "remember it, cold, in a new tab" into "press Back": Back
returns to the site with the held question restored from `#q=`, Forward
resumes the room. The "(opens in a new tab)" announcements go with it.
Pre-ship live check owed on the deployed engine, as for the Table.

### 5.4 Privacy — making the promise exact

- No query string anywhere on the site's own door (§5.1), so no server —
  including the site's own host — ever receives the question. The
  alternative (a no-JS GET fallback writing `?q=` on the site's own origin)
  would put the question in Cloudflare's logs for the JS-off minority; under
  the reasoning of Mark's ruling it is rejected, at the cost that a JS-off
  visitor's question is preserved in the input but not held. Marked
  RECOMMENDED because it is a consequence of a ruling, not a new one.
- `cic-website/_headers` gains `Referrer-Policy: strict-origin` (defense in
  depth; fragments never appear in referrers anyway).
- The returning-visitor flag is a single `localStorage` key set only when the
  visitor follows an app link, read in `try/catch`, never sent anywhere; the
  Privacy page says so (storyboard §6).

### 5.5 The offered questions — ruling 13

Six P-cell canon questions beneath the input, each a real link. Today each
holds its text and lands on the seven (option A: no default). The three
options the defense put to Mark are §10, ruling 13, with D3's recommendation:
A now; B (one disclosed citation-link per question where a record has a
source — four of six today) as a content track that shortens the path most
at the least cost in honesty; C (a pilot default voice) never, absent
evidence. Under any option the door opens only when §5.2 lands.

---

## 6. Typography, colour, motion

### 6.1 Type

Two faces, the locked pair; no third. Alegreya SC is not used (the 01/03
stretch is moot).

| Role | Face | Size / leading | Notes |
|---|---|---|---|
| Body (homepage) | Alegreya | 1.0625rem / 1.65 | |
| Reading column (tradition page) | Alegreya | 1.125rem / 1.6 on a 38rem measure | 01's reading conditions |
| H1 | Alegreya 500 | `clamp(2rem, 4.5vw, 3rem)` / 1.12 | a title, not a bold headline |
| H2 | Alegreya 500 | `clamp(1.6rem, 3.2vw, 2rem)` / 1.15 | |
| H3 — homepage era heads (×2) | Alegreya Sans 600 | 0.8125rem / 1.15 | uppercase, letterspaced .12em, muted; the dates beside them weight 400, no transform |
| H3 — homepage margin notes (×4) and disclosure columns (×2) | Alegreya Sans 700 | 0.8125rem / 1.15 | uppercase, letterspaced .08–.1em, ink |
| H3 — tradition page, the silences (×5) | Alegreya Sans 700 | 1.05rem / 1.15 | uppercase, letterspaced .06em, ink |
| H3 — tradition page, the record's sub-heads (×8) | Alegreya 700 | 1.15rem / 1.15 | |
| H4 — Representative names (×7) | Alegreya 700 | 1.25rem / 1.15 | the role beside the name in muted sans |
| Labels, chrome, sidenotes, captions, eyebrows | Alegreya Sans | 0.8125–0.95rem | **never below 0.8125rem (13px)** |
| Buttons | Alegreya Sans 600 | 1rem | |
| Wordmark | Alegreya 700, *in* italic 400 | 1.2rem | |

`text-wrap: balance` on headings, `pretty` on reading paragraphs; no
justification; no drop caps; no small caps; no old-style figure feature.
The five H3 rows are the computed styles read from the rendered reference
(the review's R2): the first issue's single "H3 / H4 · 1.15rem / 1.25rem"
row would have set the era heads and the margin notes in serif, and read
as two sizes rather than a size and a leading. Every sans label on either
page — including the offered-questions heading (storyboard §1.2h) — is
uppercase and letterspaced, never small caps.

### 6.2 Colour — the locked palette, plus the usage layer V2 adds

The hex values are the brand's and are untouched. What V2 adds is the usage
layer the D1 closure said the site needs: which token may set text, on which
ground, at what size. Every pair below was re-derived from the hex values by
D3 (WCAG relative luminance) and matches the hybrid's §6 to two decimals in
every row; the rendered DOM was walked separately (§12).

**Light register** — grounds parchment `#F6F6F2` (P) · vellum `#FFFFFF` (V) ·
gold-wash `#FBF2E2` (GW). **Change order, 2026-09-02** (Decision-Log): P and
V were re-picked at Mark's request — less yellow, a plainer paper/card pair
— while GW and every other token on this page (including the seven tradition
tints below) are untouched; every ratio in the P and V columns below is
recomputed against the new pair, not the original `#F7F3EB` / `#FEFCF8`
(every number moved up, none down):

| Token | Hex | P | V | GW | Rule |
|---|---|---|---|---|---|
| iron-gall | `#2A2521` | 13.99 | 15.16 | 13.65 | text, any size (AAA) |
| ink-faded | `#6C6257` | 5.50 | 5.96 | 5.37 | secondary text ≥13px |
| madder | `#A13E2B` | 5.98 | 6.48 | 5.83 | action: links, focus ring, the one filled button (vellum on it 6.48) |
| madder-deep | `#7E2F20` | 8.37 | 9.07 | 8.17 | hover |
| tyrian | `#6B3FA0` | 6.82 | 7.38 | 6.65 | the lexicon apparatus; draft tags (sandbox only) |
| lapis | `#1E40AF` | 8.05 | 8.72 | 7.85 | the participant's own words: *Your question, held:* |
| gold-leaf | `#B45309` | 4.63 | 5.02 | **4.52** | **rules and ≥18.66px-bold only — never small text** (the 0.02 margin on gold-wash) |
| graphite | `#8A837C` | 3.45 | 3.74 | 3.36 | **control borders only** (≥3:1 as a boundary); never text |
| rule | `#E6DFD3` | 1.22 | 1.32 | 1.19 | hairlines between blocks; **never on an interactive element** |

**Dark register** — ground `#17130F` · surface `#1E1913` · leaf `#241C13`:

| Token | Hex | ground | surface | leaf | Rule |
|---|---|---|---|---|---|
| text | `#F1E9DD` | 15.35 | 14.49 | 13.95 | text |
| muted | `#B8AEA1` | 8.45 | 7.98 | 7.68 | secondary |
| action | `#E08C74` | 7.19 | 6.79 | 6.54 | links, focus, button edge — the live site's own value (`style.css` 346); ruling 6 |
| hover | `#F0A98F` | 9.48 | 8.95 | 8.62 | |
| gold | `#E0A458` | 8.47 | 7.99 | 7.69 | rules |
| tyrian | `#C9A6E8` | 8.89 | 8.39 | 8.08 | lexicon |
| lapis | `#9DB4F0` | 8.99 | 8.49 | 8.17 | held question |
| control | `#A39B92` | 6.74 | 6.36 | 6.13 | borders |
| button | `#F6EFE0` on `#A13E2B` fill | 5.66 | | | the fill is 2.85 vs ground / 2.69 vs surface — **the 1.5px `#E08C74` edge (7.19 / 6.79) is the control's boundary**; 1.4.11 is met by the edge, by design |
| the mark | `#EDE5D6` / `#CB6E52` | 14.76 / 5.18 | 13.94 / 4.89 | | the Logo Usage Sheet's own dark register, for the mark only |
| dark rule | `rgba(241,233,221,.16)` | — | | | hairlines only, as in light |

**The seven tradition tints — rings and one left rule only, never text, in
either register — colours unchanged by the 2026-09-02 ground/surface change
order above.** Light, on the new parchment: House-Churches `#7c3aed` 5.26 ·
Alexandria `#2B5F8A` 6.24 · Syriac `#b45309` 4.63 · Church and Empire
`#7A2E2E` 8.59 · Desert `#0f766e` 5.05 · Cappadocian `#A0522D` 5.18 ·
Bethlehem `#9d174d` 7.28 — all ≥3:1 as rings. In dark the raw values fail as
rings (Church and Empire 1.99, Bethlehem 2.34, Alexandria 2.73, all seven
under 3.7). **Proposed dark tints** (ruling 7 — new values, derived, not
brand-approved): `#955FF0` · `#3B83BF` · `#CC5E0A` · `#C36060` · `#128D84` ·
`#C46437` · `#E23B7F` — each ≥4.5:1 on the ground (4.54–4.60), 4.29–4.34 on
the surface, 4.13–4.18 on the leaf. The corrected sentence: **≥4.5:1 as text
on the ground only; ≥3:1 as rings on every ground, which is their only use.**
These belong in the census as a `colorDark` field, not in a stylesheet.

Rules that ride with the tables, binding:

- Graphite never sets text below 24px (or 18.66px bold) on any ground.
- Gold-leaf never sets small text; where the Representative's pigment is
  wanted beside a label, it is a rule, and the label is ink.
- `--rule` never distinguishes an interactive element (no underline, no sole
  border of a control).
- Tints never set text; in dark they are the `colorDark` values.
- Every text node is measured against its *painted* ancestor background, not
  the page ground; a washed or surfaced block is measured on its own ground.
- The live stylesheet's `--muted #6B6259` (4.45 on the Era-I ground) is not a
  V2 token; secondary text is ink-faded / dark muted, and never on an era
  ground on this site (era grounds are the Atlas's).
- The re-set exchange on the homepage (storyboard §1.4d) departs from the
  constitution's §4.1 transcript grammar in two named ways, both forced by
  this usage layer: the Representative's label is ink with a gold-leaf rule
  beside it, not "a gold small-caps label" (gold-leaf never sets small text;
  no small caps — ruling 19); and the Facilitator's lines are italic in
  ink-faded, not "graphite" (graphite never sets text). The grammar's shape
  — name above flowing prose, no bubbles, the participant's "You" in lapis —
  is kept exactly. Ruling 21 carries the note.

### 6.3 Motion — the whole inventory, binding

| What | Moves? | Reduced motion |
|---|---|---|
| The "Arriving" mark, homepage hero, once per page arrival — byte-faithful to `CiC_Logo_Arriving_Motion_Reference.html` (800ms wait · 1300ms build · 600ms sit · then the breath) | once | the completed still mark |
| The header | nothing — wordmark only, so the mark never plays twice | — |
| The tradition page | nothing — no mark, no motion | — |
| Hover, focus, current | instant colour or border change | — |
| Lexicon card, Level-3 panel, held block | appear and disappear instantly | — |
| Scroll | native; no smooth scroll (it rides keyboard focus); no snap | — |

Nothing else transitions, reveals, lifts, slides, or dims — by omission in
the stylesheet, not by a global override. Verified by enumerating every
element's computed `animation-name` and `transition-duration`: homepage
exactly two animated elements carrying three animation-names (`cic-buildC`
on the ring; `cic-sitdown` and `cic-breath` on the seat), zero transitions;
tradition page zero and zero; under `prefers-reduced-motion` zero on both
(§12). A verifier asserting "two" by name would fail; it asserts two
elements and these three names. The mark's autoplay on arrival is ruling 16.

### 6.4 The restraint discipline, with its reasons

- **Figures never fade in, lift, glow, or dim, on any surface** — the
  constitution's anti-ghost principle (§2.5a) "governs everything visual
  with a figure in it," and the site has figures in it. Carried with its
  reason, not as taste. It extends to the Atlas's portraits (the 02 defense's
  rule; it indicts `atlas-v3.html`'s 18% trace-dim, and goes into that track
  as its own ruling).
- **No reveal-on-scroll, no hover lift, no transitions as a default, instant
  state changes** — house style, kept because it reads as unhurried; labelled
  house style, not constitution.
- **One filled control per screen**; secondaries are text links with a
  1px current-colour underline.
- **Nothing sticky** — the two device-specific amputations D2 measured (01's
  running head, 03's seat bar) cannot recur, and 2.4.11 holds by
  construction.

### 6.5 The dark register — ruling 6

The website keeps a dark register. The constitution's "dark mode: deferred"
governs the app; the live site ships dark mode today on every page
(`style.css` 336–354), and removing it would be the deviation. What V2 rules
is that the site has **one** dark register — the measured table above —
replacing the five ad hoc attempts D1 produced and the per-page overrides the
live site has accreted (`index.html` 48, `support.html` 204,
`pilot-feedback.html` 29: three separate fixes for the same un-redefined
`--muted`). Inside it, one open question for Mark: the site's dark action
colour is `#E08C74` (7.19), the brand's sanctioned dark madder is `#CB6E52`
(5.18, the mark's). D3 recommends keeping `#E08C74` for links and action —
higher contrast, live precedent, and the Logo Usage Sheet's dark pair is
written for the mark — with `#CB6E52` reserved for the mark's dot.

---

## 7. Accessibility floor — binding rules

### 7.1 WCAG 2.2 AA, with four criteria held higher

1. **7:1 for running prose in both registers** (1.4.6 as practice): iron-gall
   13.70, dark text 15.35. Not full AAA — madder as link text is 5.86, and it
   is the brand's action accent.
2. **3:1 for every graphical boundary** — rings, control borders, button
   edges, underlines — in both registers. This is where four of five D1
   directions failed in dark mode; every such element is measured.
3. **The 13px floor enforced, not declared** — the verifier walks every text
   node (§7.3).
4. **No sticky chrome at all**, so 2.4.11 Focus Not Obscured holds by
   construction.

### 7.2 The rules

- **R-A1 Reflow.** No horizontal scroll at 320px, either register, any page.
- **R-A2 Contrast.** 4.5:1 minimum for every rendered text node against its
  painted background (3:1 at ≥24px or ≥18.66px bold); 3:1 for every
  boundary that carries meaning; both registers.
- **R-A3 Size.** Nothing under 13px carries meaning.
- **R-A4 Targets.** ≥24×24 everywhere; ≥44px on every padded control (buttons,
  nav links — the tradition page's breadcrumb links included, which the
  reference sets at 34px and the build pads to 44 — chair actions, the
  input, question links, the panel close). **Lexicon terms, and the ✲
  wherever it is a control, carry a 44px padded hit area** — the
  constitution's §2.4 and §7 item 9, carried to the site's own lexicon. The
  reference does not give them one (the four terms measure 74×29, 86×29,
  67×29 and 92×29 at 390); the build adds a transparent `::before` that
  extends the hit box without moving the text, and §7.3 measures it. Inline
  links in running prose ride SC 2.5.8's inline exception and are not
  claimed at 44 (the corrected sentence — the hybrid's overstatement,
  withdrawn).
- **R-A5 Names.** Every link's purpose from its text alone: every "Ask" names
  the person; every record link carries the tradition's name (visually
  hidden where the visible text is "Her record →"); every question link
  carries "— ask *Name*" on the tradition page.
- **R-A6 Outline.** One H1; no skipped levels; every Representative a
  heading; the outline reads as the page's argument.
- **R-A7 Focus.** 2px madder / 3px offset outline (≥5.86 light, 7.19 dark);
  no positive `tabindex`; Escape closes and returns focus; nothing hidden
  contributes a tab stop; a hidden Level-2 card never swallows focus (hold
  `aria-expanded` while focus is anywhere inside the term's wrapper).
- **R-A8 Announce.** State changes the visitor caused are announced by
  moving focus (the held block), never by a live region on a block toggled
  from `hidden`.
- **R-A9 Timing and motion.** No timing, no interruptions, no animation from
  interaction (2.2.1, 2.2.4, 2.3.3); reduced-motion parity.
- **R-A10 Without JavaScript.** Every name, every app link, every section
  present in static markup; the door degrades to a jump that preserves the
  input.
- **R-A11 Level 2 for everyone.** A lexicon term is a `<button>` whose
  accessible *description* is the gloss, so a screen reader hears Level 2
  whether or not the card is painted (verified in the accessibility tree).
- **R-A12 Landmarks and skip.** Skip link first; `<main>`, `<nav>` labelled,
  `<footer>`; the first Tab after the skip link lands inside `<main>`.
- **R-A13 Images.** Real alt text on every portrait; decorative SVG
  `aria-hidden`.
- **R-A14 Print.** Every section of the tradition page prints; header, seat
  line, actions, panel and skip link hidden.

### 7.3 The verifier — what D4 runs before every push

The measurement pass that the hybrid ran and the review extended, as a
standing script plus one human step:

1. Overflow at 320 / 360 / 390 / 414 / 480 / 640 / 768 / 820 / 900 / 1024 /
   1099 / 1280 / 1440, light and dark.
2. Every rendered text node's contrast against its painted background, both
   registers, both pages; fail on < 4.5 (< 3 large).
3. Every text node's computed size; fail on < 13px.
4. Every element's `animation-name` and `transition-duration`; the inventory
   must equal §6.3, and be empty under reduced motion.
5. Heading outline; tab-stop count and sizes; accessible names of every
   link; the accessibility tree at rest and after a hold.
6. The door flow, with and without JavaScript; the lexicon flow by keyboard
   and by touch.
7. **A screenshot pass, looked at** — the header's missing space survived
   every scripted check and was visible in the first screenshot (the
   review's lesson).
8. In the real faces, on a real device or a device-mode render with the
   fonts loaded, before ship: the fold positions in §3.3 were measured in
   fallback faces.
9. The hit box of every lexicon term, ✲ control and breadcrumb link, ≥44px
   (R-A4) — the one target class the reference fails.
10. Reading level of every drafted participant-facing line (Flesch-Kincaid)
    against the Brand Guidelines' 10th-grade floor; the record apparatus
    (storyboard §2.8f–h) may run higher and sits one screen deep. For the
    record: the D2 reviews measured the hybrid at 8.2 (homepage) and 10.1
    (tradition page); the D3 review measured D3's drafted copy at roughly
    grade 5–6, the apparatus at 11–15.

---

## 8. Responsive system

The constitution's two breakpoints govern: **≥900px desktop; <640px phone;**
between them the single column narrows. Within that, the site's own
secondary breakpoints, each doing one job:

| Breakpoint | What changes |
|---|---|
| ≤480 | chair portrait 56px |
| ≤640 | header padding tightens and the nav sets at .9rem with tighter gaps — header 163px at 320–390 (the wordmark's row above two nav rows), 114px at 414–480 (above one), 65px at 640 (one row; §4.2); side-door long text hidden; Level-3 panel becomes a bottom sheet (≤55vh, transcript visible above); gravities stack; status grid single column |
| ≥640 | status grid two columns |
| ≥760 | disclosure block two columns |
| ≥900 | homepage exchange: leaf + margin notes side by side; tradition title block: text + portrait plate |
| ≥1100 | tradition sidenotes float into a reserved 17rem margin; Level-2 card anchored beside the term (fixed popover above the thumb below 1100) |

Columns: `--wide` 64rem for chrome; `--col` 44rem for sections; `--measure`
38rem for reading. Phone gutters 1.25rem. Nothing is sized in vh except the
bottom sheet's cap. Full per-page behaviour is in the storyboard.

---

## 9. What is still sacrificed, said plainly

- **The typed question does not travel — yet.** Until the app reads `#q=`,
  the visitor types it twice. The page says so. The day it lands, the door is
  finished; the site cannot finish it alone.
- **The seven are still chronological.** Under a question, not instead of
  one — but a visitor who wants "which of these is for me" gets no ranking
  until the router exists or ruling 13 is made.
- **The tradition page is long on a phone** — 16,683px at 390×844 with the
  AI line above the seat line (about twenty screens), the five silences
  carried whole (673 words of statements plus their source notes) and the
  record in full. The chair is offered at 1,368px and again at the end; an
  in-page contents list is recommended (ruling 22) so the length is
  navigable. That is Chloe's page. The silences run 2 to 7 per tradition
  (storyboard §2), so the Cappadocian page carries three sections where
  Chloe's carries five and Church and Empire's eight; the length moves with
  them, and "the silences, whole, said first" is the rule at three and at
  eight alike — no accordion at eight, no padding at three.
- **Only Chloe's record page exists in the reference implementation.** The
  pattern is one page; the content is seven, and each tradition's record must
  clear ruling 4 before its page ships.
- **The portraits are unresized masters** (3.4MB for 72px rings). Production
  needs sized, lazy-loaded portraits — a build task.
- **No Level-2/Level-3 on the homepage's captured exchange.** It is a picture
  with a caption saying so; the real grammar is on the tradition page.
- **No map band, no seat picker on the homepage.** Seating happens in the
  app behind one quiet link; the map is one link until the Atlas is on the
  brand tokens.
- **The offered-questions list may date.** Its content is what saves it.
- **The homepage is 1,900 words visible, 9,441px at 390×844** (6,786 at
  1280) — a long page for a first-time visitor, deliberately front-loaded.

---

## 10. The rulings register

Every named "ruling for Mark" the hybrid (README §8, 1–12) and its defense
(§5.4, 13–20) accumulated, plus the items the review and defense named
without numbering and the decisions the record left to D3. Nothing dropped.
Rulings 34–39 were added at the D3 review (its R7, R8, R9 and R11); the
storyboard's own page-level ⚠ items are all here (37–39).

| # | Ruling | Status | D3's position |
|---|---|---|---|
| 1 | **The question door outranks the other S0 doors on the website.** The constitution's S0 makes three doors co-equal, "no default"; this site gives "Start with your question" the first surface, "choose a voice" the second screen, the Table a quiet third. | **⚠ OPEN FOR MARK** — a stretch of a FINAL document | RECOMMENDED: adopt the ranking for the website only. It is taken from Mark's own 2026-09-02 words and the five-for-five D2 finding; the app's own S0 stays co-equal and is not this workstream's. Said plainly (the review's r7): the constitution's three doors are *your question · build your own table · guided onboarding*; the site keeps two, substitutes the chronological picker for the middle rank, and drops guided onboarding because it is not built (D0 note; hybrid README §10). |
| 2 | **Seed-status canon questions on a public surface.** All 23 P-cell questions are `canon_status: seed`, already served inside every live conversation. | **⚠ OPEN FOR MARK** — content clearance | RECOMMENDED: clear the six for the homepage (no new exposure); the internal status word never appears on the page. |
| 3 | **The W1 Guided Starters draft** ("awaiting Mark's review, not deployed") supplies three of the tradition page's seven questions. | **⚠ OPEN FOR MARK** — content clearance | RECOMMENDED: the template ships with cleared questions only; the three starters join when that draft is reviewed. |
| 4 | **Record text at `status: draft` on a public page.** Every field the tradition page quotes — silences, witness texts, terms, the guard line — is draft in the store; so are all seven traditions' records (156–259 records each, all draft). | **⚠ OPEN FOR MARK** — the biggest content gate in V2 | RECOMMENDED: the template freezes now; each tradition's page ships when its quoted records clear the record store's own gates, labelled as the record's. Paraphrase is not an option — trimming or softening a silence is the edit a doubter would catch. |
| 5 | **The question in the deep link — the mechanism.** | **DECIDED as to mechanism** — see 14 | Build item for the app (§5.2). Whether and when the change order is built is *not* decided — that is ruling 34. |
| 6 | **Dark mode.** One measured dark register for the site (§6.5); inside it, `#E08C74` vs the brand's `#CB6E52` for action text. | RECOMMENDED (keep a dark register) · **⚠ OPEN FOR MARK** (which action colour) | Keep `#E08C74` for links and action; `#CB6E52` for the mark only. |
| 7 | **The seven derived dark tradition tints** (§6.2) — new values, not brand-approved. | **⚠ OPEN FOR MARK** — brand approval | RECOMMENDED: approve as `colorDark` census fields, rings only. |
| 8 | **The mark leaves the header;** appears once, in the hero, with its public sentence beside it at caption size; the header carries the wordmark with the italic *in*. The sentence is therefore the first text on the page — an explicit choice under the Logo Usage Sheet's caption rule, not an inherited one. | RECOMMENDED — it is the fix for the two Logo Usage Sheet breaks the Decision-Log records against the live header | Mark to confirm the departure from the live header convention at the freeze. |
| 9 | **"Where it stands on the Creed"** on the tradition page, last in the confidence section (the 02 defense's position). The audience question — vetting board, or the absence of a trap? — is unsettled. | RECOMMENDED (keep, last, once) · **⚠ OPEN** (the audience question) | Test it with the people it is for: add one line to the pilot feedback form's "confusing" prompt rather than guess. |
| 10 | **"I want to believe in Jesus, but I can't. What would you say to me?"** — sixth of six on the front door. | **⚠ OPEN FOR MARK** | RECOMMENDED: keep, placed last. A person's question; the subject is the subject. |
| 11 | **The `?mode=table` links.** Multi-voice Table verified in the shipped frontend, not on the deployed engine. | RECOMMENDED: keep, with the pre-ship live check | Copy promises nothing about the experience. |
| 12 | **The "welcome back" line** (`localStorage`, `try/catch`). | RECOMMENDED: keep, with the gated side door (both on the same flag); described on the Privacy page | Cut both if Mark prefers no device storage at all. |
| 13 | **The offered questions:** (A) no default, hold and hand the visitor the seven — built; (B) one disclosed citation-link per question where a record has a source (four of six today); (C) a pilot default voice. | **⚠ OPEN FOR MARK** | RECOMMENDED: A at launch; B as a content track (source mapping per question, per tradition — the tradition page already does this for Chloe); C not, absent evidence — a default is a choice made for the visitor without disclosure. |
| 14 | **Where the held question rides to the app.** | **DECIDED — the fragment `#q=`, never a query string** (Mark, Decision-Log 2026-09-02) | Protocol in §5.2; the site's own hold is also fragment-only (§5.1, §5.4). |
| 15 | **Same-tab hand-off** on every app link. | RECOMMENDED (§5.3) | Pre-ship live check on the deployed engine's rehydration. |
| 16 | **The mark's joining plays on arrival.** The Logo Usage Sheet: "the motion never replays unbidden and never plays the joining at a visitor" — "the joining" is undefined in the brand files; the brand's own reference file autoplays the full sequence once. | **⚠ OPEN FOR MARK** — brand interpretation (the 04 defense's stretch item, restored) | RECOMMENDED: keep the single autoplay on arrival, byte-faithful to the reference; reduced motion gets the still mark. Mark defines "the joining" for the record. |
| 17 | **The two "world" record quotes** on the tradition page. | RECOMMENDED: bracketed elision — "a later [tradition]" — with the record cited beside it, until `task_9222cdbc` fixes the record layer; then verbatim | Verified: zero visible "world" on the converged page. The same discipline now covers the guard line's opening sentence (storyboard §2.5d, the review's R4): the cut is declared on the page in the source note, with the record cited, and the tag no longer says "verbatim" unqualified. |
| 18 | **The single-seat Table href** (`?worlds=X&mode=table`) lands on a disabled "Seat at least two voices." The live site's own per-Representative link has the same landing. | RECOMMENDED: keep the link with landing-state copy (storyboard §2.2/§2.9); file the live-site defect separately | A documented pairing would need `pairings.ts` (itself DRAFT) — not now. |
| 19 | **The four antiquarian devices** — Roman numerals, drop caps, a colophon, small caps — excluded on the hybrid's reading of "nothing antiquarian," argued for by both the 01 and 03 defenses. | **⚠ OPEN FOR MARK** | RECOMMENDED: exclude. The 01 review's "illuminated codex" finding is about accumulation, and Mark's non-religious-feel ruling makes the accumulation risk real on this subject. |
| 20 | **The pilot/cost copy itself** — "a limited number of participants… about five conversations" — a scarcity register the Never list names, on the homepage in any position. | **⚠ OPEN FOR MARK** | RECOMMENDED: move below the seven (done, the live order) *and* re-draft in a capacity register without scarcity shape (storyboard §1.3 offers the draft). |
| 21 | **The captured exchange's ground.** The hybrid sets it on `--gold-wash` in a bordered box; the constitution removed gold-wash from the transcript ("remain in the palette for any washed grounds elsewhere"). | RECOMMENDED: set the leaf on vellum (`--surface`) with the hairline border — a quoted leaf that shows the app's own no-wash grammar, and no argument about "elsewhere" | Either reading is defensible; vellum contradicts nothing. The leaf's label grammar also departs from §4.1 in two ways the usage layer forces — ink with a gold rule for the Representative's name (no gold small text, no small caps), italic ink-faded for the Facilitator (graphite never sets text) — named in §6.2 (the review's r8). |
| 22 | **"Where we are quiet" — whole, or opened from the first two sentences?** (Left to D3 by the hybrid.) | RECOMMENDED: whole. 673 words of statements; the cost is the page length in §9. Add an "On this page" contents nav under the seat line. No accordion — an accordion hides a silence. | |
| 23 | **The 02 defense's optional homepage map band** (left to D3). | RECOMMENDED: not in V2. One link. Revisit once the Atlas is on the brand tokens; building it now re-enters the palette debt on the homepage. | |
| 24 | **A Representative's portrait is never dimmed, on any surface.** | RECOMMENDED as a binding site rule (§6.4); carried into the Atlas track as its own ruling (it changes `atlas-v3.html`'s 18%) | |
| 25 | **The protected hook's capitalisation** — Brand Guidelines and the live H1 say "Church"; the constitution's S0 quotes "church." | Note, not a ruling: the FINAL brand text governs; V2 uses "Church" | A drift in the constitution's own record, noted for that thread. |
| 26 | **The phone header wraps to two nav rows** (163px at 320–390: the wordmark's own row above two nav rows; 114px at 414–480 above one — §4.2) rather than a menu button or a hidden scroller. | RECOMMENDED (measured) | Paid once; not sticky. |
| 27 | **A "Traditions" index page and a "Method" page** (the 03 defense's items 8–9). | RECOMMENDED: not in V2's page set — the homepage's chairs section (deep-linkable at `#who`) is the index; About's "How it works" is the method. A Method page is a candidate for a later increment if About grows. | |
| 28 | **A branded 404 page.** | RECOMMENDED: add (storyboard §9). | |
| 29 | **`Referrer-Policy` in `_headers`.** | Build item under ruling 14 (§5.4). | |
| 30 | **No-JS door behaviour** — jump and preserve, no query string. | RECOMMENDED (§5.4, a consequence of 14) | The alternative named there. |
| 31 | **The offered-questions list as the period-risk surface.** | Note. Content saves it; the build watches it. | |
| 32 | **A preview deployment for D4** — the charter's Render assumption was wrong (D0 seam A); `cic-website/` deploys via a **Cloudflare Worker with static assets** (Workers Builds' Git integration — corrected 2026-09-02, change order; not the classic "Pages" product this ruling originally named), which supports per-branch previews the same way, gated on the Production branch setting. | **⚠ OPEN FOR MARK** — console action, already logged; restated because D4 cannot start safely without it | Confirm the Production branch is `main` and check the Deployments tab for a preview URL on `claude/website-v2-sandbox`. |
| 33 | **The six historical-site photos** (D0 seam B). | Untouched; none used in V2 | No change. |
| 34 | **Authorising the `#q=` change order in `cic-poc/frontend`** (§5.2 — roughly fifteen lines across three or four files, a test, a Render deploy). Ruling 14 decided the transport; the Decision-Log says the build "is D4's to build when this increment is scheduled, not done here." | **⚠ OPEN FOR MARK** — a change order against the app, outside this workstream's own repo (the review's R11) | RECOMMENDED: schedule it with D4's first increment. Until it lands the door's interim clause stands, the visitor types the question twice, and the site's most important promise is half-kept. "Authorise this direction" and "authorise one line in `App.tsx`" are the same decision. |
| 35 | **Should a free entry point surface the Table at all?** D0's seam G: the V1 log's 2026-07-24 rule kept the multi-Representative Table out of the free interview entry point as a planned paid tier; the live homepage has since put "Bring *Name* to the Table" beside every free interview link under Mark's 2026-08-28 launch ruling (`index.html` 63–65, 313–317) — a loosening that was never confirmed as one. V2 designs entry points around the loosened reading: the third door (storyboard §1.3k) and two Table links on every tradition page (§2.2d, §2.9d). | **RULED 2026-09-03 — no gate. Free and prominent, confirmed.** Mark: rule on it directly, rather than leave D3's recommendation standing unconfirmed. No paid tier for the multi-voice Table in this pilot. Reasoning on record in the Decision-Log: this confirms the live site's own 2026-08-28 precedent rather than reversing it; the pilot's entire cost strategy elsewhere is an honest ask, not a technical gate ("we're asking each participant to keep to about five conversations… we can't enforce this yet, only ask" — 1.3j), and a hard paywall would need account and payment infrastructure this pilot has nowhere else, for a feature whose whole point is showing traditions in dialogue to the broad, curious audience the pilot exists to hear from. Revisit only if real usage data during the pilot shows the cost is actually unsustainable. | `table.html` (built 2026-09-03), the homepage's second door, and both tradition-page Table links all stand as built, unconditionally. Ruling 18 stays live (not moot). |
| 36 | **The reviewer's-brief material on the tradition page** — the sources table, the gravities, the contested list and the four "press first" questions (storyboard §2.8e, f, h, k) — is arranged from `Ministry/Scholarly-Review/CiC_World1_Brief_for_Reviewers_Source.md` for Chloe, and from that folder's `CiC_WorldBrief_{Desert,Hieronymian,Syriac}_V0_1_DRAFT.md` for three more. **Alexandria, the Cappadocian Churches and Church and Empire have no brief.** All four files are drafts written for outside reviewers, in public-safe form by their own account; none has been cleared for a participant surface. | **⚠ OPEN FOR MARK** — content clearance, alongside 2, 3 and 4 (the review's R7) | RECOMMENDED: clear the W1 brief's arranged material with Chloe's page. For the other six, the brief-derived sub-sections ship only when that tradition's brief exists *and* is cleared; until then they are absent from that page (the census-derived sub-sections stand), and the review-status line does not say "a reviewer's brief is on file" where none is. This narrows what the template promised, and the storyboard now says so (§2.10). |
| 37 | **`whats-next.html`'s meta description** still says "three new worlds in development" — the count and the tradition-not-world rule both apply (storyboard §5, S.6). | **⚠ OPEN FOR MARK** — live copy; a wording Mark owns (the review's R9) | RECOMMENDED: "two new traditions in development" in the pending-push wording, or whatever that fix settles on. |
| 38 | **`whats-next.html` and `support.html` contradict each other on the Atlas's scope** — the first says Church in History "currently covers the traditions Church in Conversation has built or plans to build"; the second describes the map that shipped 2026-08-03 across all 292 census entries (storyboard §5). | **⚠ OPEN FOR MARK** — one of the two live sentences is stale; D3 does not know which Mark wants (the review's R9) | RECOMMENDED: the `support.html` sentence, which matches the census and the shipped map. |
| 39 | **One footer line on every page** — the entity line (storyboard S.3). Today `support.html` carries "A ministry in formation." and `pilot-feedback.html`'s footer omits Feedback and Privacy. | **⚠ OPEN FOR MARK** — a copy change on two live pages (the review's R9) | RECOMMENDED: the entity line everywhere; it is the line the entity facts favour. |

---

## 11. Dependencies, separate tracks, and build notes

### 11.1 The app change order — `#q=`

§5.2. Its own decision to schedule, its own repo and deploy. Until it lands,
the door's interim clause stands and no site copy claims the question
travels.

### 11.2 The Atlas rework track

The 02 defense's §5.1 brief, referenced, not re-executed here: the converged
token block (chrome on brand tokens, era bands on the ten approved grounds,
`--ink-faded-ground #4A433C`); DOM-as-document (prerender from the census;
script upgrades); per-stop accessible names *and* headings; deep link per
tradition with `pushState`/`popstate`; all five census edge types in words
and a third stroke for tension; the portrait rule (ruling 24); the phone
list form with the toggle hidden below 900; Level-2 on touch as a non-modal
popover with a real "Full entry" control; the 13px floor in the panel;
opaque sticky era heads; the Creed note kept and last, the key teaching only
what is on screen; zero outbound links. Plus its cross-cutting findings
(`ground`/`groundDark` census seam; the `edgeRow()` rule). V2's homepage and
storyboard are consistent with that track existing: one link, the name
"Church in History," the nav label "Map."

### 11.3 Data fixes at the source (`world-census.json`)

The site renders dates, names, tiles and tints from the census at runtime;
fixes go there, never on a page:

- Dash characters are inconsistent: five built entries carry en dashes,
  Chilo's and Marius's carry hyphens (`c. 325-394 CE`, `c. 312-451`), both
  era heads carry hyphens; Marius's entry has no era marker. Pages render
  the data verbatim; the fix is a data fix.
- The Bethlehem Circle's `sourcing` still says "Richest written record of the
  **four** built worlds" — queued as `task_959d6df4`.
- A `colorDark` field per built tradition (ruling 7).
- Record-store ids differ from census ids for two traditions
  (`cappadocian-trinitarian` / `cappadocian-nicene-pastoral-monastic-tradition`;
  `imperial-juridical` / `imperial-juridical-christianity`): the tradition
  page joins census data by census id and records by record `world_id`; the
  build must not assume they match.
- The Cappadocian entry alone carries `statusWord: "Built & Live"`,
  `glyph: "live"` and a portrait `.jpg` in `entry.icon`, where the other six
  live entries carry `"Open for conversation"`, `null` and a world-icon SVG
  (PR #74's census fix was made for the Atlas display). Rendered as the
  storyboard's §2.1e specifies, Chilo's status line would read "Built & Live
  — you can sit down…" — project jargon on a participant surface (the
  review's r9). The page never renders an internal status word: the status
  line is drafted from `statusWord` only where it reads "Open for
  conversation," and the fix is in the census, not on the page.

### 11.4 Content gates

- Rulings 2, 3, 4 (canon, starters, draft records) and 36 (the reviewer's
  brief material — four traditions have a brief file, three have none).
- `whats-next.html`'s Cappadocian correction and the two "six traditions"
  counts (`index.html`, `about.html`) — done in a worktree, **not yet
  pushed** (Decision-Log 2026-09-02). V2's What's Next and About assume they
  have landed: seven live, two in development (Latin Pastoral, Donatism).
  Two more items on the same page are Mark's: its meta description (ruling
  37) and its Atlas sentence against `support.html`'s (ruling 38).
- `task_9222cdbc`: "world" in the record store's spoken text.

### 11.5 Deploy

Ruling 32 (Pages preview); `_headers` gains `Referrer-Policy: strict-origin`;
the existing `no-store` on HTML and `/data/*` stands.

### 11.6 Build notes found while verifying

- `.site-nav a{display:inline-flex}` overrides the `hidden` attribute; the
  gated side door needs `.site-nav a[hidden]{display:none}` or the gate is
  silently defeated.
- The side door's missing space: fix with `gap:.3em` on the anchor (an
  `&nbsp;` inside the span also works; `gap` is cleaner). Measured 4.55px at
  ≥768.
- Chromium blurs the focused element before focusing the next; a Level-2
  card hidden on blur swallows keyboard focus — hold `aria-expanded` while
  focus is anywhere inside the wrapper (the hybrid's fix; verified).
- The Level-3 panel's `<h2>` is empty at rest; `visibility:hidden` keeps it
  out of the accessibility tree — keep it that way (never `opacity:0`).
- Portraits: ship sized masters (≥2× the 72px ring, and a 4:5 crop for the
  tradition page's plate), `loading="lazy"`, `decoding="async"`.
- All fold positions were measured in fallback faces (§0.3); the real
  Alegreya has a larger x-height — re-measure with the fonts loaded.
- The `#q=` fragment: §5.1's rule, verbatim — decode in `try/catch`, trim,
  cut to 280, `textContent` only. One cross-feature seam (the review's
  r15): an "On this page" link (storyboard §2.3) is a fragment navigation,
  so it replaces `#q=`, and a share or bookmark taken after it loses the
  question. With JavaScript the contents links scroll by script and leave
  the hash alone (`preventDefault`, `scrollIntoView`, focus moved to the
  heading with `tabindex="-1"`); without JavaScript they are plain anchors
  and no question was ever held, so nothing is lost.
- Inline-mark hit areas (R-A4): the lexicon `<button>`s and the breadcrumb
  links need a padded hit box the reference does not give them (29px and
  34px tall respectively at 390).
- The side door on the tradition page: the hybrid's `tradition-chloe.html`
  leaves it ungated (no `hidden`, no `id`); the shared chrome gates it on
  every page, as S.2 specifies.

---

## 12. Verification record — what D3 measured

Scratch copies of the hybrid's two files were built in the session
scratchpad with the fixes the defense specified (nothing in the repository
was modified): the fold fix (the door's H2 and input directly under the H1;
the lede beneath the input; the hero's first sentence moved to the chairs'
scope line), `gap` on the side door, the side door gated on the returning
flag, the pilot and cost paragraphs below the seven, seven distinct record
link names, focus to the held block, the protected line once per section,
the distress line once per page, the in-tab disclosure, the dated caption,
the fragment-only hold with no `<form>`, the input named by the H2, **the
phone chrome tightened — below 640px the nav at .9rem with `gap:0 .85rem`
and the header row's gap `.1rem 1rem` — and the hero/door padding tightened
for the fold (hero `2rem 1.25rem .5rem`, door top `.75rem`, the door's inner
padding 1rem at ≤640, input basis 11rem)** — the chrome change the first
issue of this list left unnamed (the review's R3) — and on the tradition
page the orphaned `#lexhint` deleted and the two "world" quotes elided.
Chromium `chromium-1194`, Playwright, fallback faces.

**Fold (converged homepage, first-time visitor, sandbox note stripped):**

| Viewport | Header | Input top–bottom | Lede | First offered question |
|---|---|---|---|---|
| 320×844 | 163 | 537–585 | 674–812 | 1,201 |
| 360×800 | 163 | 456–504 | 574–684 | 1,029 |
| 390×844 · 740 · 660 | 163 | 456–504 | 574–684 | 1,005 |
| 414×896 | 114 | 408–456 | 526–636 | 957 |
| 768×1024 | 73 | 364–412 (button on the same row) | 428–483 | 671 |
| 1280×800 · 1440×790 | 73 | 455–503 | 519–574 | 762 |

The input is in the first screen at every viewport tested, including
390×660 and 320×844; the lede is fully in the first screen from 740 and its
first line is visible at 660. The unfixed hybrid, re-rendered for the
record: input at 897px at 390×844, exactly the review's number. The header
column is corrected at the fix pass: the first issue printed 110 / 61 / 41,
which were these heights minus the sandbox note's (53px on phones, 32 on
desktop) — the note sits above the header and does not change it. The
position columns were note-stripped correctly and are unchanged; with the
hybrid's own untightened nav the review measured 168 / 118 / 73 and the same
fold conclusion. Nav links are 48px tall at ≤640 and 49px above, inside a
65–73px one-row header, so S.2's 44px rule and these heights agree.

**Overflow:** 0px at 320 / 360 / 390 / 414 / 480 / 768 / 1024 / 1280 / 1440,
light and dark, both pages.

**Contrast, every rendered text node against its painted background:**
homepage 175 nodes, minimum 5.37 light (ink-faded on gold-wash), 5.66 dark
(button text on the madder fill), zero failures; tradition page 266–267
nodes, minimum 5.39 light, 5.66 dark, zero failures. The hex-derived tables
in §6.2 match the hybrid's to two decimals in every row.

**Size:** nothing under 13px on either page in either register.

**Motion:** homepage two animated elements, three animation-names
(`cic-buildC` on the ring; `cic-sitdown`, `cic-breath` on the seat), zero
transitions; tradition page zero and zero; reduced motion zero on both.

**Structure:** homepage outline H1 → H2 (door) → H2 (who) → H3 ×2 → H4 ×7 →
H2 ×4, no skipped levels; 40 tab stops (the side door hidden for a first
timer; a real Tab walk, not only an enumeration), none under 24×24 except
inline prose links; tradition page **32** tab stops with the side door
gated as S.2 specifies — 33 with it ungated, as the hybrid file leaves it,
which is the figure the first issue printed and the review reproduced; the
storyboard's keyboard path had also miscounted the breadcrumb as three
links (it is two: the current page is text). Seven record links, seven
distinct accessible names; seven "Ask" links naming the person; zero app
links before the AI line for a first-time visitor. The skip link's next Tab
lands on the question input.

**The door:** typed + Enter → `#q=…` in the URL, empty search string, the
held block visible, focus on the held block (name: "Your question, held:" +
the question), next Tab → "Edit it"; the landing screen at 390×844 reads
held question · Edit it · Who's at the table · Who would you like to ask? ·
scope · era head · Chloe — no pilot paragraph, no cost paragraph; the first
"Ask Chloe" 770px below the landing point. An offered question → the same.
Arriving with `#q=` → restored. Empty submit → scroll, nothing held. Without
JavaScript → jump to `#who`, input preserved, no URL written, 7 names and 10
app links present, side door hidden.

**The lexicon:** focus a term → `aria-expanded="true"`, card shown, the term
described by its gloss; Enter → panel open, focus on Close; Escape → panel
closed, focus on the term. Touch: first tap → fixed popover at 621–824 of
844, second tap → panel. The orphaned `#lexhint` is gone; "world" appears
zero times in the visible text.

**The side door:** hidden for a first-time visitor at every width; for a
returning visitor, a 4.55px gap between "Been here before?" and "Go straight
in →" at ≥768; for returning visitors only, the side door costs a nav row
from 414 to 900 (measured at the fix pass: header 163px at 414–480, 114 at
640, 174 at 700, 125 at 768–900; 73 from 1024, as for a first-time visitor).

**Looked at:** screenshots at 390 light and dark, 1280 light, the
after-submit landing zone, the returning header, the tradition page at 390
and 1280 — the door is in screen one, the held block reads as the
constitution's R0, the header's gap is visible.

**Measured at the fix pass (the review's R1, R3, R5), same Chromium, same
faces, sandbox note stripped:**

- *The homepage's launch state* (ruling 4: Chloe's page only, six chairs
  with one action) — a scratch copy with the six other record links removed:
  **34 tab stops** for a first-time visitor by a real Tab walk (40 in the
  end state, re-walked the same way), one record link, seven "Ask" links,
  header 163px at 390; every other figure unchanged.
- *The tradition page with the AI line above the seat line* (storyboard
  §2.2a, the shared phone chrome, the side door gated) at 390×844: header
  169px (the hybrid's tradition file differs from its homepage by a few
  pixels of chrome; the build has one stylesheet); the AI line 1,268–1,352;
  the seat line 1,368; the first app link ("Begin a conversation with
  Chloe") 1,443 — **after** the AI line for a first-time visitor; "An AI
  system, speaking for a whole people" 1,622; the silences 2,402; the
  questions 5,971; "In her own words" 7,715; the record 9,279; the closing
  door 16,046; page height 16,683; overflow 0 at 320, 390 and 1280; eight
  H3s in the record section. The first issue's tradition landmarks
  (1,348 · 2,383 · 5,952 · 9,260 · 16,027 · 16,663) were taken with the
  sandbox note present — 75px on that page at 390 — contrary to Appendix
  B's own caption; the figures above are stripped, as the caption says.
- *The `#q=` rule (§5.1), against the reference script, arriving at the
  converged homepage with each fragment:* `#q=` and `#q=%20%20%20` →
  nothing held, the fragment dropped; `#q=%E0%A4%A` (undecodable) → nothing
  held, the URL untouched; three hundred characters → held at 280, the
  input at 280, the fragment rewritten to those 280; `<b>`, `<img
  onerror>` encoded → held as text, **zero elements** inside the held block;
  a normal question → held, restored, no scroll on arrival.
- *Contrast, re-walked on both fix-pass copies with the note and the
  sandbox draft marks stripped:* tradition page with the AI line, 264 text
  nodes, minimum 5.39 light / 5.66 dark, zero failures, nothing under 13px
  — the new line is ink on parchment and sets no new minimum; homepage in
  the launch state, 163 nodes, 5.37 / 5.66, zero failures.

---

## 13. What happens next

1. Opus reviewed this synthesis and the storyboard against the charter, the
   constitution, and the struggle record — the same discipline as every
   prior artifact (2026-09-02: ready to freeze with eleven required fixes,
   applied in this revision and named where each lands).
2. Mark reads, rules on the ⚠ items in §10 (or defers them explicitly), and
   **freezes** Website Design V2. After the freeze, changes need a change
   order.
3. D4 builds in increments on the sandbox branch (Pages preview confirmed
   first — ruling 32): the shared chrome and stylesheet; the homepage; the
   tradition template with Chloe's page (gated on ruling 4); the carried
   pages' small changes; the 404. Each increment runs §7.3 before any push
   and is read by Mark before it merges — merge means live.
4. The app change order for `#q=` is scheduled separately, on Mark's
   authorisation (ruling 34); the day it lands, the door's interim clause is
   deleted and the "Ask" hrefs carry the question.

*— D3 synthesis, 2026-09-02; fix pass the same day, after the Opus review.
Every number above was measured on a scratch render after the fixes were
applied — and re-measured where the review found a slip; every quotation
was opened at its source; nothing outside this file and the storyboard was
written.*
