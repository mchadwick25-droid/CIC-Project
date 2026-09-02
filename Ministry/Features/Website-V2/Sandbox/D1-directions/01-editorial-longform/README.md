# D1 Direction 01 — Editorial / Long-Form Storytelling

**Sandbox artifact, 2026-09-02. Not a deliverable. One of several independent D1 directions, written without sight of the others.**

Files: `homepage.html` — the issue: front matter, opening essay, contents, seven chapter openings, four essays, the door, colophon. `representative-chloe.html` — the key inner journey: one Representative's full introduction as a feature essay, reusing the app's lexicon and citation grammar. Both open directly from disk. Portraits are referenced relatively from `cic-website/assets/portraits/`; everything else is inline. Copy tagged `draft` is mine and unreviewed; the brand's protected lines appear verbatim and untagged; the seven traditions, Representatives, dates, regions, and colors are hand-copied from `world-census.json` as of today (seven live, Cappadocian included).

## The philosophy

The site is a book, and the visitor is a reader. Specifically, a literary quarterly whose first issue is *The First Centuries*: front matter, a contents page, two Parts, seven chapters, a few essays, a colophon. Each Christian tradition is a chapter, and each chapter is opened by its Representative in their own voice, the way a good anthology lets a contributor speak before the editor does. The prose does the persuading. There is no hero-and-button stack, no feature grid, no carousel, no tiles. There is a running head, a reading column, plates, marginal notes, and one door.

Why this rather than a "nice editorial feel" on a marketing template: the product's own constitution already calls the Table "a beautifully set trade book on parchment" and the transcript "a printed dialogue that breathes." A visitor who reads the site as a book and then sits at the Table arrives already inside the register. The site stops being a brochure *about* the experience and becomes its first pages. That is the whole bet, and it costs things, named below.

Three consequences, pushed rather than softened:

1. **Sequence over navigation.** The seven Representatives are met in chronological order, inside two Parts with their own part-title pages. You meet Chloe first because 70 CE comes first. Each chapter opening is a spread — plate on one side, text on the other, alternating recto/verso down the page.
2. **The apparatus is visible, in the margin.** "It shows its work" is the brand's second message, so the site shows its work the way a scholarly edition does: ✲ markers in the text (the app's own citation mark), sidenotes floated into the outer margin at ≥1100px and set inline below that. On the Chloe page, lexicon terms carry the app's exact Level-2/Level-3 grammar — Tyrian dotted underline on first occurrence, hover/focus for the short card, click for the full entry in a side panel (bottom sheet on phone), never a modal.
3. **One door, always in the same place.** "Come and join us at the Table" sits in the running head of every page, in madder, and returns once as the closing line of the issue and of each chapter. Each chapter also carries a quiet "begin a conversation with X · bring X to the Table" line. That is the entire CTA inventory.

## How it serves the four goals

**Accessibility.** Long-form reading *is* the design, so the reading conditions are the system: 20px Alegreya at 1.55 on a 38rem measure (≈62–66 characters), old-style figures, true paragraph indents, nothing under 13.6px carrying meaning. Because everything is prose, running text is held to AAA (7:1), not merely AA — iron-gall on parchment is 13.7:1. A page with no competing surfaces is also a page a screen-reader user can traverse by headings alone: masthead → contents (a real `<nav>` of in-page links) → Part → Chapter → essay; every chapter is an `<article>` labelled by its title. Sidenotes sit inside the paragraph directly after their marker, so they read in order without jumping. Reduced motion removes every transition; without JavaScript nothing is hidden.

**Clear storytelling.** The goal this direction is built for. The opening essay carries the argument in five paragraphs and raises the AI question itself, first, in the third — before any Representative speaks. Each tradition then gets what a tile cannot give: a dateline, its approved one-sentence description, and a first paragraph in its own voice that shows what "let the world speak" sounds like — Chloe keeping the bishop-or-council question open, Marius refusing to say which see wins. The Chloe page is the full payoff: a "we" voice that keeps disagreement visible, a section titled *Where we are quiet* that treats the tradition's absent stories as part of the story, and "Where the historical record is thin, we let the silence stand" used as an epigraph, not a slogan.

**Easy access to features.** Argued, not assumed. The contents page lists every chapter, essay, the Atlas, and the door in reading order, one screen below the masthead — a returning visitor is one click from anything. The running head keeps the door at top right at every scroll position without asking for attention. Each chapter hands off directly into the app with its tradition pre-seated. What the direction refuses is *multiplying* entry points: one door, always in the same place, is easier to find than four doors in four styles.

**Professional, cutting-edge design that draws people in.** The most distinctive thing this site can look like, against every other faith-tech and nonprofit site, is a well-set book. Where "cutting-edge" usually means motion and gradient, here it is typographic craft: a real masthead, part-title pages, decorative roman numerals set in the rule color behind each chapter, plates with tradition-colored bookmark ribbons, dotted-leader contents, hanging punctuation, small caps from the same superfamily. The slow reveal is the only motion — the page turning, never performing.

## What it sacrifices, honestly

- **Speed to first click.** The door is visible from the first pixel, but the page's rhythm asks a visitor to read. Someone who wants a conversation in ten seconds gets less encouragement here than any other plausible direction offers. Pilot recruitment (four perspectives, about five conversations) is one quiet paragraph under the closing line, not surfaced early.
- **Scanability, especially on a phone.** Seven chapter openings make a long homepage; on a phone the spreads stack and it is genuinely long. The contents page mitigates; it does not cure. A grid says "seven" at a glance — this says it over several screens.
- **The Atlas becomes a fold-out, not a spine.** An essay with a link. A visitor the map would have caught first is served worse.
- **Content volume, forever.** Every Representative now needs a real, reviewed feature essay — seven now, nine soon — and the direction is only as good as those essays. The draft-and-approve discipline that already rewrites support copy several times a week would be signing off long prose in a Representative's voice for every tradition. Real editorial labor, ongoing.
- **Cost/support is a colophon paragraph.** Deliberate, per seam F (six rewrites in a week): one content slot, two links, nothing in the layout depends on its wording.
- **Portrait resolution.** The locked portraits are 511–748px square; at plate size on a 2× display they read soft. Higher-resolution masters or an accepted painterly softness — a production call.

## Typography, color, motion — inside the locked system

**Type.** Alegreya for every reading and display size; Alegreya Sans only for apparatus (running-head links, captions, sidenotes, draft tags). Scale is pushed: the masthead wordmark to 5.4rem, the hook and chapter titles to ~3rem at weight 400 (a book title, not a bold headline), the door line to 3.6rem, drop caps opening every essay. Small-caps labels use **Alegreya SC**, the small-caps cut of the same OFL superfamily — proposed for Mark below, not assumed.

**Color.** Palette untouched. Parchment ground; vellum for the running head, panel, and footer; iron-gall for all prose. Madder does what the constitution says: links, the door, focus rings. Gold-leaf marks the Representative's voice — the small-caps "Chloe · Household Leader" label and the rule beside her paragraph — exactly as the app labels a Representative turn. Tyrian marks the apparatus: ✲ markers, lexicon terms, the Level-3 panel. Graphite appears only as a hairline, never as text (3.38:1 on parchment fails). Per-tradition census colors appear as the plate ribbon (non-text) and the chapter kicker; all seven pass AA on parchment (4.54–8.40:1), the weakest being Mar Yausep's #b45309.

**Motion.** Two things move. Blocks reveal once as they enter the viewport (1.1 s, 14px rise, never re-hidden; off under reduced motion; absent without JS). The "Arriving" mark plays the brand's own sequence once, in the colophon, beside the one public sentence — first-contact rule observed, never on a photograph. Nothing pulses, follows the cursor, or moves to attract a click. The table-and-chair glyph is not used, so the adjacency guard is never tested.

## Accessibility floor

**WCAG 2.2 AA throughout, with AAA (7:1) contrast for all running prose.** The higher bar on prose follows from the philosophy: a direction whose whole persuasion is long text has no excuse for text that is merely legal. Measured on parchment `#F7F3EB`: iron-gall 13.70 (prose); ink-faded 5.39 (large italic standfirsts, captions ≥13.6px, apparatus — AA); madder 5.86 (links); tyrian 6.67; gold-leaf 4.54 (small-caps labels ≥14.4px only). Dark register on `#17130F`: `#F1E9DD` 15.35, `#B8AEA1` 8.45, `#E08C74` 7.19, `#E0A458` 8.47, `#C9A6E8` 8.89 — all above 7:1. Beyond contrast: 2.2's focus appearance (2px madder outline, 3px offset) and focus-not-obscured (`scroll-padding-top` clears the 56px sticky head); target size ≥24×24 on every inline control; no dragging anywhere; skip link, landmarks, a heading outline that reads as the book's contents; reduced-motion parity; and a print stylesheet — a quarterly should print.

## Proposed stretches, for Mark to rule on

1. **One door, not the app's three.** The constitution's S0 threshold has three co-equal doors; this direction hands off to the app's Table field (`?mode=table`) through a single sentence and lets the three doors live in-app. If the three-door threshold must be visible from the marketing site, the closing section changes.
2. **Chapter handoffs carry both links** — `mode=interview` and `mode=table` — inheriting seam G unchanged. If the old gate still stands, the second link is cut everywhere with no layout consequence.
3. **Alegreya SC.** Within the family the brand names, but not on its list.
4. **Lexicon Level-3 on the marketing site** means a web-facing copy of lexicon entries; the mockup's are drafts. Either the site reads the same records the app reads, or the essays keep only the hover card.
5. **The Atlas palette debt** is inherited and paid at build: the map should read as this book's fold-out, on the era-ground palette the constitution already assigns it.

Nothing here contradicts the constitution's app rules; the site reproduces neither the Table, the Living Table scene, modes, nor guided onboarding, and no copy promises them.
