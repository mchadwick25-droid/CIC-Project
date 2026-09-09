# 02 — The craft and visual quality bar: what "made with real care" looks like on simple technology (2025–26)

**Workstream:** Website V2 · **Kind:** research brief (input to a design pass; decides nothing) · **Date:** 2026-09-08 · **Researched by:** Fable, per the model-routing ruling (deep research) · **Companion:** `01-narrative-invitation-design-patterns.md` (structure and pacing; this brief is the *surface* — type, image, motion, colour, phone)

**Why this brief exists.** Mark has ruled that the surrounding website must be redesigned around heart, story and invitation, and that it must match or exceed the craft already reached in the Atlas and the conversation UI — "top of the line, professionally built." The live site is plain HTML, one 9.9 KB stylesheet, vanilla JS, and two Google-Fonts families (Alegreya and Alegreya Sans; one page still loads Cinzel), maintained by a very small team. So the question this brief answers is narrow and practical: **what does current (2025–26) top-tier craft look like for editorial, typography-forward, story-led sites that get a premium feeling out of fundamentally simple technology — and which of those moves can this team make in well-written CSS, considered typography and a little vanilla JS, without a framework?** Five areas were researched: typography as the primary tool; imagery for historical and religious subject matter; restrained motion; warm light/dark theming; and mobile-first pacing for slow reading. It ends with a ten-item craft checklist, each item tied to evidence, and a short note on where the evidence touches rulings already frozen in `CiC_Website_Design_V2.md`.

**How the research was done, honestly.** The sandbox's egress proxy blocked direct fetches of nearly every reference site (craigmod.com, publicdomainreview.org, plough.com, emergencemagazine.org, gwern.net, utopia.fyi, stephango.com, typewolf.com, webkit.org, MDN, web.dev, Smashing, A List Apart, alistapart, nngroup.com, awwwards.com, and about twenty-five more). Three kinds of source *did* work and every claim below rests on one of them, tagged inline:

- **[platform data]** — browser-support and Baseline status read from the raw `web-features` and `caniuse` data files on GitHub (fetched directly, exact versions quoted), plus the Chrome team's own cross-document view-transitions guide (GitHub).
- **[maker's account]** — a studio, agency, award, press release, foundry, or author describing what they built and why, retrieved through web search of the indexed page text (quoted where possible), or fetched directly from GitHub (Emil Kowalski's animation standards and review skill; Vercel's animation guidance; the Flexoki palette; Utopia's core library; the Standard Ebooks Manual of Style typography chapter).
- **[critique / research]** — a published analysis, usability study, or trend retrospective, via indexed page text.

Where a design observation about a site is my inference from those sources rather than something I saw rendered, it says so. §8 lists the URLs D-work should open in a real browser and screenshot into `Sandbox/` before anything is imitated. The web-search budget was exhausted at 200 queries; nothing below was written from memory alone.

---

## 1. The bar in one paragraph

The sites that read as "made with care" in 2025–26 are not the ones with the most effects; they are the ones where **the typography is doing the work a framework would otherwise be hired to fake**. A serif with a lineage set at a real book measure and leading; headings that wrap on purpose; quotation marks, dashes and small capitals that are the right glyphs; an image that is an actual artifact, large, cropped with intent, captioned with its source; motion so scarce that the one thing that moves is remembered; a dark register that is warm ink on warm paper rather than a product's night mode; and a phone layout that was designed, not reflowed. Every one of those is a CSS-and-HTML decision. The current platform has quietly caught up to this: `text-wrap: balance` and `pretty`, `light-dark()`, `@starting-style`, fluid `clamp()` scales, `hyphens: auto` unprefixed on iOS, and opt-in cross-document view transitions are all deliverable from a static site with no build step [platform data]. The craft bar, in other words, is now reachable by a small team — provided it is held as a discipline rather than added as decoration.

---

## 2. Typography as the primary design tool

### 2.1 What the best story-led sites are doing

**Emergence Magazine** — emergencemagazine.org · [maker's account]. Designed by Studio Airport (Bram Broerse, Maurits Wouters) when the magazine "shift[ed] from quarterly issues to publishing content online weekly." Typefaces on record: GT America (sans), LL Bradford (serif), Windsor, and Studio Airport's own PG Titling — i.e. a character-carrying serif for voice, a neutral sans for apparatus, and a display face reserved for titling. On the photo-essay template the studio says it "struggled to find a format that provided the immersive experience" and, "after several prototypes, landed on a **traditional vertical scroll format with ample space for images**, paired with several enhanced interactions." Webby and National Magazine Award (Ellies) nominations for "Best Editorial/Digital Feature." The lesson is not the specific fonts; it is that a studio with an award-winning motion vocabulary *chose* a plain vertical scroll with room to breathe for its most contemplative content.

**Aeon and Psyche** — aeon.co / psyche.co · [maker's account]. Aeon has long been the reference for "long-form intellectual content with clean typography and focused reading experience" (Siiimple's indexed description). Psyche's May 2025 relaunch (design by Liquorice, Melbourne; built by Aeon's in-house team) is the most useful recent case: the stated problems were that "the structure made it difficult to explore freely and follow their curiosity" and that "on mobile in particular, the experience lacked the fluidity needed to support deep engagement"; the stated fixes were "more expressive typography," a palette "updated to feel more human and inviting," and a strategy of "exploration over chronology and clarity over clutter." That is a 2025 editorial team naming, in its own words, the exact axis CiC is moving along — warmth and expressiveness *within* a reading-first system.

**Lapham's Quarterly** — laphamsquarterly.org · [maker's account / critique]. A magazine that "brings up to the microphone of the present the advice and counsel of the past" — historical texts and historical art, which is CiC's material. On the Responsive Web Design podcast the team said the reading experience "was one of the most important things when the magazine was being designed on print, so it was considered, for the first time really, to have as a wonderful reading experience online." Described in critique as "scholarly, bookish," "very traditional and academic." Worth studying as the *cautionary* half of a pair with Psyche: bookish is right; bookish-and-airless is the failure mode.

**gwern.net** — gwern.net · [maker's account]. The strongest evidence that plain technology can carry the highest typographic bar. A static Hakyll site with "4 design principles: aesthetically-pleasing minimalism, accessibility/progressive-enhancement, speed, and a 'semantic zoom' approach to hypertext"; "monochrome esthetics, sidenotes instead of footnotes on wide windows, efficient dropcaps, smallcaps, collapsible sections"; dark and reader modes. Critically: "JavaScript is not required for the core reading experience, only for optional features like popups & transclusions, table-sorting, and sidenotes, and pages can be read without much problem in a smartphone or text browser." Two hard-won lessons on record: a dark-mode rewrite "took 3 months" whose only reader-visible change was "removing slowness" (speed *is* the craft); and the experiment with red headers/links/dropcaps in dark mode "looked like a 'vampire fansite'" to readers and was removed (see §5).

**Craig Mod** — craigmod.com · [maker's account]. Essays set in a single column with the typography adjusted over years ("changes to font sizes, layout grid updates, and overall simplification"). His 2011 *A Simpler Page* / Bibliotype work (A List Apart) introduced the **Bed / Knee / Breakfast** reading distances — close to the face lying down, on the knee on a couch, propped on a table — and argued that serious long-form reading software should set margins, line lengths and sizes for each. It remains the clearest articulation of why a phone-reading layout must be *designed* for the distance it is held at (§6).

**Plough** — plough.com · [maker's account]. The most craft-conscious Christian editorial site on record. Its own "Retooling the Plough" note describes the redesign: "editors and designers agreed that it was time to refresh the design, especially the logo and typography," and that a "more compact nameplate would greatly expand the possibilities of art they could use" — the nameplate was shrunk *to make room for the art*. Creative direction: Clare Stober. **Ekstasis** (ekstasismagazine.com, Christianity Today) describes itself as "a kind of digital cathedral, a sanctuary from the noise, a place that captures our attention through loving art and luminous words" — the register CiC's charter is reaching for, stated by a peer.

**The Guardian (2025)** — theguardian.com · [maker's account]. Its "biggest redesign in a decade" is the mainstream proof that print typography and phone-first are not opposites: "75% of their digital readers visit daily using a mobile device," and the response was "mobile-first UX with print-inspired art direction," letting "sections have their own visual identity through typography and layout variations" to fix "the 'everything looks the same' problem."

**Piccalilli / Set Studio (Andy Bell)** — piccalil.li, set.studio · [maker's account]. The methodological source for doing all of this on a small team: "creating type scales that respond to the viewport, rather than setting explicit values for typography and space, allows you to set rules once and forget about them"; CUBE CSS as "a progressive enhancement approach... the end-goal is shipping as little CSS as possible." The one-line creed of his *Build Excellent Websites* manifesto: "Be the browser's mentor, not its micromanager."

### 2.2 The numbers that recur

These are the settings the sources above and the standard references converge on for narrative prose; the CiC values already frozen in Design V2 §6.1 are shown beside them.

| Setting | Evidence | CiC V2 today |
|---|---|---|
| Measure (line length) | 45–90 characters including spaces; "regardless of screen width, the optimal line length is still 45–90" (Butterick, *Practical Typography*) [critique] | 38rem column at 1.125rem ≈ 62–70 characters in Alegreya — inside the band |
| Body size, web | 15–25 px (Butterick); 17–18 px "delivers a more comfortable reading experience" for long-form; never below 16 px on phones (2025 mobile-typography guides) [critique] | 1.0625rem (17 px) homepage / 1.125rem (18 px) reading column — on target |
| Leading | 120–145% of size (Butterick); 1.4–1.6 for long-form on phones; some guides go to 1.5–1.8 for mobile [critique] | 1.65 / 1.6 — at the generous end, which suits a serif with a large x-height |
| Fluid scale | Utopia's method: choose min/max viewport (e.g. 320→1240 px), min/max base (e.g. 18→20 px) and min/max ratio (e.g. 1.2→1.25), derive every step as a `clamp()`; `utopia-core` also returns a `wcagViolation` list naming the viewports where a step cannot be zoomed to 200% (SC 1.4.4) [maker's account] | Headings use hand-written `clamp()`; body is fixed. A single Utopia-generated scale would let the site and the Atlas share one set of steps |
| Margins | "Web pages need big margins to preserve text legibility"; "the edges of the screen are not the end" (Butterick) [critique] | — |

### 2.3 The finish: what separates "set" from "styled"

The **Standard Ebooks Manual of Style** (typography chapter, fetched from GitHub) is the most complete public rulebook for book-grade text on screen, and almost all of it is copy discipline plus a few lines of CSS [maker's account]:

- Typographer's quotes always; the right single quotation mark (U+2019) for elisions; periods and commas inside closing quotes.
- Em dashes (U+2014) unspaced for parentheticals; en dashes (U+2013) for ranges; a real minus (U+2212) for negatives; the ellipsis glyph (U+2026), not three periods.
- **Small capitals for era designations — "BC, AD, BCE, CE: set without periods, in small caps"** — and for acronyms pronounced as words; times as "a.m./p.m." in lowercase with periods. For a site whose every page carries dates like "AD 325," this single rule is the difference between a book and a web page.
- A no-break space between a number and its unit; ampersands preceded by a no-break space.

Two further finishes are now platform features rather than tricks [platform data]:

- **`text-wrap: balance` on headings** — Baseline; Chrome 130 (partial from 114), Firefox 121, Safari 17.5; 86.9% global. **`text-wrap: pretty` on paragraphs** — not Baseline; Chrome 117, **Safari 26 / iOS 26**, Firefox not yet; falls back harmlessly. WebKit's implementation evaluates the whole paragraph (rags, rivers, short last lines), Chrome's the last lines only — so the effect is now *stronger* on the iPhones most visitors carry than it was when V2 was frozen. V2 already specifies both.
- **`hyphens: auto`** — unprefixed on iOS 17+ and macOS Ventura+ Safari; use it on the reading column below ~40 characters so word spacing stays even. **`hanging-punctuation: first last`** — Safari-only, one line, harmless elsewhere; opening quotation marks hang into the margin as they do in a printed book.

**Drop caps.** The literary convention is one drop cap per chapter opener, three lines deep in "literary and historical" settings, two in contemporary non-fiction [critique]. On the web the proper mechanism, `initial-letter`, is **not Baseline**: Chromium 110+ (unprefixed from 133), Safari 9+ only with `-webkit-` until 18.3 and unprefixed after, **Firefox none**; a caniuse note warns that some implementations ignore the web font and fall back to a system face for the initial [platform data]. gwern ships "efficient dropcaps" regardless [maker's account]. If CiC wants them, the honest implementation is `initial-letter` behind `@supports`, with a float-based fallback, tested in the real Alegreya — or none at all. V2 currently rules none (§9 notes this as an item the new brief may reopen).

**Pull quotes.** They work as "entry points for scanners" (NN/g F-pattern research, cited in editorial guides) and give long text rhythm; the current pattern is a side pull quote that floats beside the column on wide screens and stacks on phones, set larger with *tighter* leading, contrasting with the body "without breaking the brand voice," and never mistakable for a headline [critique]. For CiC the natural pull quote is a `[RECORD — verbatim]` line — provenance beside it, per the storyboard's guard rule.

**The face itself.** Alegreya — the pair CiC already owns — was designed by Juan Pablo del Peral (Huerta Tipográfica) and "originally intended for literature," with "a dynamic and varied rhythm which facilitates the reading of long texts," referring "to the calligraphic letter, not as a literal interpretation, but rather in a contemporary typographic language"; it was one of 53 "Fonts of the Decade" at ATypI Letter.2 (2011) and among its top 14 text systems [maker's account]. The research does not suggest changing it. It suggests *using more of it*: the V2 table sets every heading and label as either Alegreya 500/700 or Alegreya Sans uppercase, which is correct, but a literature face also has italics for the Representative's voice, a display-size cut for one title per page, and (in its designed companion, Alegreya SC, or the `smcp` feature if the served build exposes it — verify) the small capitals the era designations need. The current pairing pattern of the best sites — character serif for voice, neutral sans for apparatus, at most one titling moment — is exactly the two-family system already locked; the craft gain is in range and finish, not in a third face. (One page still loads Cinzel; that is the "third face" the sources warn against and should go.)

### 2.4 Achievable in plain CSS — the pattern

A single `:root` scale from Utopia (five type steps, five space steps, all `clamp()`), a 38–40rem reading column with `text-wrap: pretty; hyphens: auto; hanging-punctuation: first last;`, `text-wrap: balance` on `h1–h3`, `font-variant-numeric` and `font-variant-caps` set deliberately per element (dates in prose vs. tables), curly quotes and real dashes enforced in copy review, and — if adopted — `initial-letter` behind `@supports`. No JavaScript is involved in any of it.

---

## 3. Imagery for historical and religious subject matter

### 3.1 The authenticity premium is now measurable

The 2025–26 evidence on generated imagery is unusually consistent [critique]: Merriam-Webster's 2025 Word of the Year was *slop*; Meltwater measured negative sentiment toward "AI slop" at 54% in October 2025; the share of consumers who prefer generative-AI creator content to human creator content fell from 60% (2023) to 26%; iHeartMedia's research found 90% of listeners "including those who actively use AI tools themselves" want media created by humans; CNN's business desk called 2026 "the year of anti-AI marketing"; Digiday reports that "authenticity and 'messiness' are in high demand." The tells that once gave AI images away ("unnatural lighting, awkwardly rendered hands") have "largely been smoothed over," which has made audiences *more* suspicious of anything smooth, not less.

For CiC this cuts deeper than taste. The product's integrity claim is that the Representative is "built from that tradition's own historical sources." A generated fresco or an imagined "ancient scroll" on the page that makes that claim would contradict it before a word is read. The imagery rule that follows is the same as the copy rule the project already lives by: **verbatim-and-flag** — real artifacts, real sources, stated.

### 3.2 What the best historical sites do instead

**The Public Domain Review** — publicdomainreview.org · [maker's account]. Founded 2011; the reference site for presenting out-of-copyright historical images as *objects of attention* rather than decoration — each essay built around a single work or archive, images large, sources credited. In January 2025 it launched the **Public Domain Image Archive** (pdimagearchive.org): "over 10,000 out-of-copyright historical images," "meticulously curated," browsable "by style, theme and era," "spanning 2,000 years of visual history," free "including for commercial purposes." Two things to imitate: images are shown *whole and large* before any crop, and every one carries its source institution.

**Rijksmuseum** — rijksmuseum.nl · [maker's account]. The 2020 site (Fabrique with Q42; Dutch Design Award gold; the Collection Online won two 2025 Webbys) is "characterized by extremely large images"; "the defining feature... is the use of full-screen illustrations of artworks in the collection, which serve as navigation tools and encourage visitors to keep clicking to uncover underlying information." 340,000+ high-resolution images downloadable free. The move is simple and cheap to copy: the artifact *is* the navigation surface; the chrome disappears behind it.

**Trinity College Dublin's Book of Kells Experience (2024)** · [maker's account]. Not a website pattern but a signal about register: "high-resolution projections, animated illustrations and audio narration to introduce the manuscript's symbolism, the monks who created it, the materials they used." The manuscript detail, enormous, plus the human story of its making — the same two ingredients CiC has for every tradition.

### 3.3 Where the real images are (open licence, early-Christian relevant)

All CC0 or "no permission required," high resolution, verified from the institutions' own indexed pages [maker's account]:

- **The Metropolitan Museum of Art** — 492,000+ public-domain images, CC0.
- **Cleveland Museum of Art** — 30,000+ CC0 images with API; "one of the finest and most comprehensive collections of early Christian, Byzantine, and medieval European art in the world."
- **The Walters Art Museum** — entire manuscripts under CC0: "deluxe Gospel books from Armenia, Ethiopia, Byzantium, and Ottonian Germany."
- **Dumbarton Oaks** — Byzantine manuscripts as digital facsimiles; the Byzantine Institute's restoration films from Hagia Sophia and the Kariye; a census of early-Christian objects in North American collections.
- **Getty Open Content** — all rights-held or public-domain images free for any purpose.
- **Rijksmuseum** — 340,000+; **Wellcome Collection** — 100,000+ historical images.
- **Princeton Index of Christian Art** (subscription; 200,000+ reproductions to AD 1400) for *finding* the object before sourcing an open image of it.

This is enough to give every one of the seven traditions a real mosaic, manuscript initial, coin, inscription, icon or site photograph — with an accession number.

### 3.4 Treatments that read as considered, and ones that read as templated

**Considered** [maker's account / critique, synthesised]:

1. **Whole, then detail.** Show the artifact large and complete once; elsewhere crop *into* it — a hand, a tessera field, an initial, a line of Greek — at a scale the museum thumbnail never reaches. The crop is the design; the same image serves the page three ways.
2. **The provenance line, every time.** Institution · object · date · licence, in the sans at the 13 px floor. On the PDR and museum sites this is what makes the image feel like evidence rather than mood.
3. **Let the object keep its colour.** Frescoes, gold ground, red ochre and lapis are the tradition's own palette; the page's warm parchment and iron-gall tokens already sit under them. Unify with *ground and margin*, not with a filter.
4. **If texture, then quiet and real.** 2026's illustration and print trends are explicitly a reaction to "AI-smooth" imagery: "grain, ink textures, linocut aesthetics, and print-style imperfections," agencies (Central Illustration Agency, IllustrationX) signing woodblock and linocut printmakers because "brands are requesting this quality" [critique]. But the same sources place the loud version — "dense dots, harsh contrast, speckled grit" — "squarely at loud work: gig posters, zines." For a contemplative site the usable end is a paper grain on the *ground* (the tokens are already parchment/vellum) or a faint grain on photographs at low opacity; never on manuscripts and mosaics, which carry their own.
5. **If illustration, then a human hand in a print idiom.** Woodcut, engraving and linocut are both the current "made by humans" signal and historically resonant with early printed scripture. Commission it, credit it, and keep one idiom across the site.

**Templated** [critique, synthesised]:

- **Duotone as a brand filter.** The technique's modern origin is on record: Collins' 2015 Spotify identity, drawn from "duotone photos from album covers and concert posters from the 1960s," built specifically "to brand third-party artist photography" so any image "looked like something from Spotify," automated by a tool nicknamed "the Colorizer." A decade on, a duotone over a fresco reads as *that* — an entertainment brand's lens — and it destroys the object's colour, which is its evidence. Not for this site.
- Stock "hands on an open Bible," glossy 3D renders, gradient-mesh or glassmorphism panels over a blurred artwork, generated "ancient scroll" scenes, and any image without a source line.

### 3.5 Achievable in plain CSS — the pattern

`<figure>` with `<img width height loading="lazy" decoding="async">` and a `<figcaption>` carrying the provenance line; `object-fit: cover` with `object-position` set per crop; optional `mix-blend-mode: multiply` so a photographed object sits on the parchment ground; a ground texture as a **tiled 256–512 px PNG at low opacity**, not a live SVG `feTurbulence` filter — "computed per-pixel... on high-DPI screens that's a lot of pixels," and "GPU-intensive, especially on mobile" [critique]. Full-bleed on phones (`width: 100vw` inside the column; §6). No image processing pipeline is needed beyond exporting two sizes with `srcset`.

---

## 4. Restrained motion and microinteraction

### 4.1 The current craft standard, in numbers

The most widely adopted articulation of "tasteful" UI motion in 2025–26 comes from Emil Kowalski (animations.dev), whose published standards and review checklist were fetched directly [maker's account]:

- **Duration:** button feedback 100–160 ms; tooltips and small popovers 125–200 ms; dropdowns 150–250 ms; modals and drawers 200–500 ms. "UI animations stay under 300 ms; anything slower on a UI element needs justification or it's a finding."
- **Easing:** "The built-in easing curves in CSS are usually not strong enough." Entering/exiting: ease-out, e.g. `cubic-bezier(0.23, 1, 0.32, 1)`. Moving on screen: ease-in-out, `cubic-bezier(0.77, 0, 0.175, 1)`. Hover and colour: `ease`. Constant motion: `linear`. **"Never `ease-in` on UI — it delays the moment the user watches most."**
- **Physicality:** "Nothing appears from nothing — `scale(0)` looks like it came from nowhere"; enter from `scale(0.9–0.97)` + `opacity: 0`; press feedback `scale(0.97)` on `:active`, 160 ms.
- **Performance:** "Only animate `transform` and `opacity`"; never `transition: all`; never animate width/height/margin/padding/top/left.
- **Frequency:** "Match motion to how often it's seen." Actions done 100+ times a day get "No animation. Ever."; tens of times a day (hover, list navigation): "remove or drastically reduce." Vercel's guidance puts it as "Raycast never animates because users open it hundreds of times a day" [maker's account].
- **Input:** "Hover animations are gated behind `@media (hover: hover) and (pointer: fine)`" so phones never get a stuck hover state.
- **Reduced motion:** "`prefers-reduced-motion` is honored (gentler, not zero — keep opacity/colour, drop movement)." Vercel's stricter variant: "every animated element needs its own `prefers-reduced-motion` media query."
- **When something is wrong, the fix order is:** delete → reduce → fix easing → fix origin → make interruptible → move to GPU → asymmetric timing (exit ~20% faster than entry) → polish → accessibility.

Rauno Freiberg's *Invisible Details of Interaction Design* (Vercel; 3,000 words) is the other text every 2025 practitioner cites — "not a tutorial nor a collection of guidelines" but observations on "the timing of animations, the physics of motion, and the predictability of gestures" [maker's account]. Its through-line matches Kowalski's: the best interaction detail is the one you do not notice.

### 4.2 What now reads as dated

Trend retrospectives for 2026 are unanimous in direction [critique]: "animations are shifting toward restraint — they respond to what users are doing rather than competing for attention"; "heavy 3D scenes, scroll-triggered effects on every section, and stacked blur effects can make a site feel slow"; kinetic typography is "more polish than substance" and "works best as a single hero-level moment rather than something applied page-wide"; "going overboard with flashy effects, parallax scrolling, or blinking buttons" is listed among outdated practices; and the line between the surviving and the fading form is drawn precisely — "scrollytelling... reacts to scroll position instead of taking control away from it — the whole difference between this and scroll-jacking, which is fading, with one working with the browser's normal behavior and the other fighting it."

### 4.3 Before / after

| Reads as 2019 | Reads as 2026 craft | Why |
|---|---|---|
| Every section fades-and-rises 600 ms as it scrolls into view | Content is simply there. The single reveal on the site is a disclosure the reader *opened*, 200 ms opacity, ease-out | Frequency rule; "scroll-triggered effects on every section" named as fatigue; unhurried reads as confident |
| Card lifts 8 px with a growing shadow on hover, 300 ms | A 120–150 ms colour change on the underline or rule, gated to `(hover: hover) and (pointer: fine)` | Hover is a tens-of-times-a-day event; phones must never see it |
| Hero image drifts at 0.5× scroll (parallax) | Fixed composition; the one motion on arrival is the "Arriving" mark, once, as V2 rules | Parallax listed as outdated; the mark is the site's single flourish |
| JS router slides pages in from the right | `@view-transition { navigation: auto }` inside `prefers-reduced-motion: no-preference`; a ~250 ms cross-fade; instant navigation everywhere else | Cross-document view transitions: Chrome 126, Safari 18.2, Firefox none, not Baseline — pure progressive enhancement, zero JS [platform data] |
| Modal pops from `scale(0)` with ease-in | `@starting-style { opacity: 0; transform: scale(0.97) }` → 200 ms ease-out in, 150 ms out; exit faster than entry | `@starting-style` is Baseline (2024-08-06; Chrome 117, Firefox 129, Safari 17.5) [platform data]; "nothing appears from nothing" |
| Headline letters scramble or slide in on load | The headline is set; `text-wrap: balance` | Kinetic type "more polish than substance"; balance is the craft |
| Autoplaying carousel of testimonials | One quotation, set as a pull quote with its source | Carousels and autoplay in every "outdated" list; a single quote is read |
| A reading-progress bar in the brand colour across the top | None, or a hairline only inside a long chapter | Designers "hate on the article progress bar": "visually distracting, especially... in a strong contrast colour," "redundant" with the scrollbar; defensible only for very long stories [critique] |

### 4.4 Platform notes for a static site [platform data]

- **CSS scroll-driven animations** (`animation-timeline: view()`): Chrome 115, **Safari 26 / iOS 26 (September 2025)**, Firefox not shipped; not Baseline, in Interop 2026; ~84% global mid-2026. They remove the JavaScript from any scroll-linked effect — but the evidence above says a contemplative site should barely have one. The legitimate uses are a hairline chapter progress or a *very* slow tonal shift on a long page; and even those need a `@supports (animation-timeline: view())` guard and a reduced-motion cut.
- **View transitions:** same-document is Baseline since 2025-10-14; cross-document (the one a multi-page static site needs) is opt-in with one at-rule per page, defaults to a cross-fade, is customised with `::view-transition-old(root)` / `::view-transition-new(root)`, can carry a shared element (e.g. the wordmark) between pages by `view-transition-name`, and is feature-detected with `'onpagereveal' in window` [maker's account, Chrome guidance].
- **`@starting-style` + `transition-behavior: allow-discrete`** replaces every `setTimeout`-to-add-a-class hack for showing and hiding panels, dialogs and popovers.

### 4.5 Relation to the Atlas

The Atlas already has a motion vocabulary (hover tooltips, detail panels, smooth interactions). "Match or exceed" means the website should not invent a second one: the same two or three durations and the same ease-out curve, expressed once as custom properties (`--ease-out`, `--dur-fast`, `--dur-base`) and shared across `style.css` and the Atlas stylesheet, so a panel opening on the map and a disclosure opening on the tradition page feel like the same hand.

---

## 5. Light and dark theming for a warm, contemplative reading experience

### 5.1 What "warm dark" is, concretely

**Flexoki** (Steph Ango, 2023; MIT; fetched from GitHub) is the reference palette for "an inky color scheme for prose and code... inspired by analog printing inks and warm shades of paper," "calibrated for legibility and perceptual balance across devices and when switching between light and dark modes" in Oklab [maker's account]. Its base ramp is the clearest public statement of what warm-paper light and warm-ink dark look like:

| Role | Flexoki | CiC V2 (frozen) |
|---|---|---|
| Light ground | paper `#FFFCF0`; base-50 `#F2F0E5`; base-100 `#E6E4D9` | parchment `#F6F6F2`; vellum `#FFFFFF`; gold-wash `#FBF2E2` |
| Light text | black `#100F0F`; base-950 `#1C1B1A` | iron-gall `#2A2521` |
| Dark ground | black `#100F0F`; base-950 `#1C1B1A`; base-900 `#282726` (surfaces) | ground `#17130F`; surface `#1E1913`; leaf `#241C13` |
| Dark text | base-200 `#CECDC3` down to base-50 `#F2F0E5` | text `#F1E9DD`; muted `#B8AEA1` |
| Accents | 600 values on light, 400 values on dark (lighter, softer) | action `#A13E2B` light → `#E08C74` dark |

The pattern CiC already has is the right one: the dark ground is a *warm near-black* (`#17130F` sits between Flexoki's black and base-950 and carries the brown of iron-gall), the surfaces step up in the same hue, and the accent is re-picked lighter and softer for dark rather than reused. What Flexoki adds is the discipline of treating both registers as **one ramp seen from both ends** — each token has a partner — and of tuning in a perceptual space (Oklab/OKLCH) so warmth survives the flip.

### 5.2 The evidence against "tech dark"

- **Halation.** "White text against pure black... can cause eye fatigue, halation (particularly affecting approximately 50% of people with astigmatism)"; "dark grays (#121212 to #1E1E1E) rather than pure black"; text at off-white rather than `#FFFFFF` "reduces optical intensity, which reduces halation while keeping readability acceptable" [critique: Level Access; Stéphanie Walter's *Dark mode & accessibility myth*]. CiC's dark text at 15.35:1 on the ground is *higher* contrast than most reading apps choose; a slightly softer body-text token (keeping labels and headings at full) is worth measuring in the real face — V2's 7:1 prose floor leaves ample room.
- **Choice, not a forced register.** WebAIM's April 2025 guidance: provide the choice and avoid forcing either mode [critique]. gwern adds the discoverability lesson: readers "don't notice [the theme switcher] on their own due to general web-clutter-blindness," so the site briefly draws attention to it [maker's account].
- **Colour in the dark.** gwern's red-in-dark experiment "looked like a vampire fansite" [maker's account]. Keep dark accents few and muted (Flexoki's 400 values; CiC's `#E08C74` and gold `#E0A458`). The seven tradition tints re-derived for dark in V2 ruling 7 follow the same logic.
- **Images are not inverted.** gwern classifies images and marks those that must not invert (`invert-not`) [maker's account]. For CiC no artifact image should ever be filtered in dark; at most the ground beneath it warms, and a photograph may sit at `opacity: .92` to take the edge off.
- **Reading apps' precedent.** Apple Books ships six themes, each with a dark variant and a "Match Device" setting; Chrome's Reading Mode added "Sepia Light" and "Sepia Dark" [maker's account]. The warm/paper register is the consumer default for *reading*, as opposed to the neutral grey of product dark modes.

### 5.3 Achievable in plain CSS and ~15 lines of JS [platform data]

- `color-scheme: light dark` on `:root` and **`light-dark()`** per token — Baseline since 2024-05-13 (Chrome 123, Firefox 120, Safari 17.5); "widely available" around November 2026. Form controls, scrollbars and the UA default colours follow automatically.
- A **three-state toggle** (System · Light · Dark): an inline `<script>` in `<head>` reads `localStorage` and sets `data-theme` before first paint (no flash); "System" *removes* the attribute so `prefers-color-scheme` governs; a `matchMedia` listener keeps System live [critique / maker's accounts: Bryce Wray 2024, Tamas Piros, Lexington 2025]. This is the same pattern the artifact viewer for this workstream already uses.
- Tokens tuned in **OKLCH** (`oklch()` is Baseline) so the two registers share hue and differ in lightness/chroma, which is what keeps dark *warm* instead of grey.

---

## 6. Mobile-first pacing for long-form reading

### 6.1 What the research says the phone does to a reader

- Comprehension of *complex* web content on an iPhone-sized screen scored **48%** of desktop in Nielsen Norman Group's study; a later NN/g study found "no practical differences" for *simple* content, and that "reading on mobile becomes more difficult as the complexity of the content increases" because readers "see less information at once, reducing context," and "need to navigate through the document, which diverts attention" [critique]. UX Magazine (2026): mobile reading is "more fragmented, more interruptible, and less forgiving of complexity."
- Three-quarters of a serious publication's readers are on phones daily (The Guardian, 2025) [maker's account]. CiC's own expectation is the same.
- The Pudding's responsive-scrollytelling guidance, still the practitioner reference: "starting with mobile first... forces you to pare down your experience to the nuts and bolts"; keep a scroll-linked sequence on phones only when its transitions are "truly meaningful, and not just something to make it pop," and then "be shorter: a few steps to grab the user and make your point and then you're out"; **"design the stacked version deliberately rather than letting it fall out of the CSS — a large share of readers get that version"**; and beware that mobile browsers "toggle the top and bottom navbars... this causes the viewport height to change" [maker's account].
- Craig Mod's Bed / Knee / Breakfast: the phone is the *Bed* distance — closest to the face — so type can be a touch smaller than the tablet-on-a-table case but the measure must be honest and the chrome minimal [maker's account].

### 6.2 The pattern the best sites converge on

1. **One column, generous side margins, no reflow-to-the-edge.** Butterick: the edges of the screen "are not the end." A 20–24 px gutter at 17–18 px Alegreya gives roughly 38–44 characters on a 375 px phone — under the 45 floor, and the correct response is to accept it, *not* to shrink the type. Add `hyphens: auto` so the rag stays quiet.
2. **Shorter sections, more heads, more air.** The NN/g "less context at once" finding argues for breaking a tradition page into more, smaller, titled movements on the phone, each with a resting point. Emergence's "traditional vertical scroll with ample space" is the same instinct [maker's account].
3. **Images full-bleed, captions in the column.** The artifact is the one thing the phone can make *bigger* than the desktop can (§3): let it run edge to edge, then return to the measure for the caption and the prose.
4. **No sticky chrome.** iOS 26 Safari shipped with fixed/sticky elements "getting misplaced" [critique]; the dynamic toolbar changes `100vh`; V2 already rules nothing sticky, and WCAG 2.4.11 (Focus Not Obscured) holds by construction. Use `100dvh` if a full-height surface is ever needed, and `env(safe-area-inset-*)` on anything that touches an edge.
5. **Targets.** WCAG 2.2 SC 2.5.8 sets 24×24 CSS px as the AA floor; Apple's HIG 44 pt and Material's 48 dp are the comfortable norm; 44 px is the right bar for the site's few controls [standards].
6. **Pacing devices that earn their place.** A reading-time line at the top of a long page; a quiet chapter list; a "resume where you were" that is nothing more than the browser's own scroll restoration. Not a coloured progress bar (§4.3).
7. **Keep the phone's own reader modes working.** Semantic `<article>`, `<h1>`–`<h3>`, `<figure>`, real paragraphs: Safari Reader and Chrome Reading Mode then render the page in the visitor's chosen sepia — which is a compliment, not a loss.

### 6.3 Achievable without JS

Everything above is HTML structure and CSS: the column, the fluid scale, `hyphens`, `dvh`, safe-area insets, full-bleed figures, `srcset`, `loading="lazy"`. The only script that helps is the theme toggle (§5.3). A reading-time line is computed at build (or by hand) from the word count and written into the HTML.

---

## 7. Synthesis — the craft checklist

Ten things every new page is held to. Each is a yes/no a reviewer can answer by looking, and most can be asserted by the same DOM-walking verifier Design V2 §7.3 already specifies.

1. **The reading column is a book column.** Body 17–18 px (1.0625–1.125 rem), leading 1.5–1.65, measure 60–75 characters at desktop and never bought back on phones by shrinking type; side gutters ≥ 20 px. *Butterick 45–90 / 120–145%; mobile guides 16–18 px, 1.4–1.6; V2 §6.1.*
2. **One fluid scale, shared with the Atlas.** Every size and space is a step from a single Utopia-style `clamp()` scale defined once in `:root`; no ad-hoc pixel sizes; every step passes the 200% zoom check. *Utopia / utopia-core `wcagViolation`; Andy Bell "set rules once."*
3. **Typographic finish is complete.** Curly quotes, real em/en dashes, the ellipsis glyph, small capitals for BC/AD/BCE/CE and acronyms, `text-wrap: balance` on heads, `pretty` on prose, `hyphens: auto` on narrow columns, `hanging-punctuation` where honoured; no third typeface (Cinzel goes). *Standard Ebooks §8; WebKit `pretty` in Safari 26; Alegreya's designed range.*
4. **Every image is an artifact with a provenance line.** Sourced from an open-licence collection (Met, Cleveland, Walters, Dumbarton Oaks, Getty, Rijksmuseum, Wellcome) or commissioned from a named human illustrator in a print idiom; captioned institution · object · date · licence; never generated, never stock, never duotoned; shown whole once, cropped into elsewhere; native colour kept. *AI-slop sentiment data; PDR / Rijksmuseum practice; Collins/Spotify duotone origin; 2026 illustration trend reports.*
5. **The motion budget is one flourish per site and ≤ 300 ms for everything else.** The Arriving mark is the flourish. Any other transition: transform/opacity only, ease-out `cubic-bezier(0.23,1,0.32,1)` or gentler, entry ≤ 250 ms, exit ~20% faster, `@starting-style` for appearances, no `transition: all`, no reveal-on-scroll, no parallax, no kinetic type, no autoplay. *Kowalski standards; Vercel guidance; 2026 retrospectives.*
6. **Hover is gated and every animation has its own reduced-motion rule.** `@media (hover: hover) and (pointer: fine)` around every hover effect; `prefers-reduced-motion` keeps opacity and colour and drops movement, per element, not by a global override. *Kowalski review checklist; Vercel.*
7. **Both registers are warm and paired.** Dark ground is a warm near-black, never `#000`; dark text is warm off-white, never `#fff`, and body text may sit a step below the maximum contrast to limit halation while holding ≥ 7:1; every light token has a dark partner tuned in OKLCH; accents are re-picked lighter for dark and kept few; artifact images are never inverted. *Flexoki; halation research; gwern's "vampire fansite"; V2 §6.2.*
8. **The visitor chooses the register, and never sees a flash.** `color-scheme: light dark` + `light-dark()` tokens; a three-state System/Light/Dark control; an inline head script sets the attribute before paint; System removes it and follows the OS live. *Baseline 2024 `light-dark()`; WebAIM 2025; tri-state pattern.*
9. **The phone version was designed, not reflowed.** One column; shorter titled movements; full-bleed figures with captions in the column; nothing sticky; `dvh` and safe-area insets where an edge is touched; 44 px targets; reader-mode-clean semantics; no progress bar. *NN/g 48%; Pudding "design the stacked version deliberately"; Guardian 75% mobile; WCAG 2.5.8; iOS 26 sticky regressions.*
10. **Speed is part of the craft.** Fonts self-hosted as subset WOFF2 (variable where available), the two above-the-fold faces preloaded, `font-display: swap` with `size-adjust` / `ascent-override` metric overrides so nothing shifts; `width`/`height` on every image; a ground texture as a tiled PNG, not a live filter; a page-weight budget per page type; the whole site still readable with JS off. *gwern's "speed" principle and its 3-month dark-mode rewrite; 2025 Web Almanac font data; feTurbulence performance warnings.*

---

## 8. Where the evidence touches frozen Design V2 rulings

This brief decides nothing; these are inputs for the Decision-Log under the new "heart, story, invitation" charter. Read against `CiC_Website_Design_V2.md` §6–7.

**The evidence supports, as frozen:** the Alegreya / Alegreya Sans pair and the refusal of a third face; the 38 rem measure, 17–18 px body and 1.6–1.65 leading; `balance` on heads and `pretty` on prose (now stronger on iOS 26 than when ruled); the 13 px floor and 7:1 prose; one measured warm dark register with re-picked accents and the tradition tints re-derived for dark; "nothing sticky"; no reveal-on-scroll and no hover lift as defaults; the single once-per-arrival flourish (ruling 16); instant hover colour change (a 120–150 ms `ease` is the more common norm, but instant is within the craft and reads unhurried).

**The evidence invites re-examination — each an open item, with a recommendation:**

- **"No small caps."** Book typography sets BC/AD/BCE/CE in small capitals, and this site is dense with them. Recommend true small caps for era designations *only*, via Alegreya SC or the `smcp` feature if the served build carries it (verify in the real face), never synthesised, never for labels — which stay uppercase-letterspaced sans as ruled.
- **"No drop caps."** They are the strongest single "book, not web page" signal and gwern ships them on static HTML — but support is partial (Firefox none; some engines ignore the web font). Recommend: prototype one, three lines deep, on the tradition page opener only, with `@supports (initial-letter: 3)` and no fallback; ship only if it renders in Alegreya on Safari and Chrome and degrades to a plain initial elsewhere. If not, keep the ruling.
- **"Panels appear and disappear instantly."** The current craft norm for a *non-figure* surface a reader opened is a ≤ 200 ms opacity-only entry via `@starting-style`, exit ~150 ms, dropped under reduced motion. This does not touch the anti-ghost principle (figures never fade) and keeps the "unhurried" house style. Recommend allowing that one narrow class, or explicitly re-affirming instant as house style with the reason recorded.
- **"Nothing transitions" between pages.** An opt-in cross-document view transition (a ~250 ms cross-fade, wordmark carried, reduced-motion gated, instant in Firefox) is the cheapest way to make the site feel like one continuous place rather than a set of documents — which is what "invitation" asks for. It is zero JS and one at-rule. Recommend a sandbox prototype and a ruling either way.
- **Dark body-text contrast.** 15.35:1 is above what most reading surfaces choose; the halation literature suggests a step softer for running prose. Recommend measuring a candidate one step down in the real face (keeping ≥ 7:1 and full contrast for heads and labels).
- **Cinzel** on the one page that still loads it is a third face and should be removed regardless.

---

## 9. What this brief could not verify, and what D-work should do next

Because the primary sites could not be rendered from the sandbox, D-work should open these in a real browser (phone and desktop, light and dark), screenshot into `Sandbox/`, and note *exactly* what is imitable:

1. **emergencemagazine.org** — a photo essay and a long essay on a phone: section spacing, image scale, caption placement, what (if anything) moves.
2. **psyche.co** (post-May-2025) — the "more expressive typography" and "human and inviting" palette; how a piece paces on mobile.
3. **publicdomainreview.org** and **pdimagearchive.org** — how a single historical image is presented and credited; the essay page's measure and pull quotes.
4. **rijksmuseum.nl** — the full-screen-artwork-as-navigation move and how it collapses on a phone.
5. **gwern.net/design** and any essay — dropcaps, small caps, sidenotes collapsing to notes on a phone, the dark-mode toggle, the reader mode.
6. **plough.com** and **ekstasismagazine.com** — the closest peers in register; typography, art placement, chrome weight.
7. **craigmod.com** (any essay) — the single-column measure and the "nothing else on the page" discipline.
8. **utopia.fyi/type/calculator** — generate the shared scale (candidate inputs: 320→1240 px, 17→19 px base, ratio 1.2→1.25) and drop it into `style.css` and the Atlas stylesheet.
9. **stephango.com/flexoki** — read the Oklab rationale and compare the two ramps side by side with V2's tokens.
10. **animations.dev** / Emil Kowalski's *7 practical animation tips*, and **rauno.me/craft/interaction-design** — the two texts the motion rules in §4 are drawn from.

Three things also need measuring in the real fonts before any of §7 is asserted by a verifier: whether Google's Alegreya build exposes `smcp` (else Alegreya SC); how `initial-letter` renders Alegreya in Safari 18.4+ and Chrome 133+; and the actual characters-per-line at 375 px with the chosen gutter.

---

## Sources consulted

**Platform support (fetched raw from GitHub)**
- web-features: `text-wrap-pretty.yml.dist`, `cross-document-view-transitions.yml.dist`, `light-dark.yml.dist`, `initial-letter.yml.dist`, `starting-style.yml.dist`, `scroll-driven-animations.yml.dist` — github.com/web-platform-dx/web-features
- caniuse: `css-initial-letter.json`, `css-text-wrap-balance.json` — github.com/Fyrd/caniuse
- Chrome team, *Cross-document view transitions* guide — github.com/GoogleChrome/modern-web-guidance (…/ui-behaviors/cross-document-transitions.md)
- WebKit blog, *Better typography with text-wrap: pretty* (indexed text) — webkit.org/blog/16547/
- MDN and web.dev pages on `text-wrap`, `@starting-style`, `light-dark()`, scroll-driven animations (indexed text)

**Motion**
- Emil Kowalski, *review-animations* skill: `STANDARDS.md` and `SKILL.md` — github.com/emilkowalski/skills
- Emil Kowalski, *7 practical animation tips* — emilkowal.ski/ui/7-practical-animation-tips (indexed text)
- Vercel Labs, *web-animation-design* skill — github.com/vercel-labs/open-agents
- Rauno Freiberg, *Invisible Details of Interaction Design* — rauno.me/craft/interaction-design (indexed text; Every.to reprint)
- Envato, *Web design trends for 2026*; Bubble, *Web Design Trends 2026: What's In and What's Out*; Wazile, *7 Outdated Web Design Trends to Avoid in 2026*; Digital Kulture, *Parallax Scrolling: Still Cool in 2026?*; webpeak, *CSS/JS Animation Trends 2026* (indexed text)
- Digiday, *Why designers hate on the article progress bar*; UX Collective, *Pros and cons of progress indicator as a scroll bar* (indexed text)

**Typography**
- Matthew Butterick, *Practical Typography* — summary of key rules; line length; line spacing; responsive web design; page margins (indexed text)
- Utopia — utopia.fyi; `utopia-core` README — github.com/trys/utopia-core; Smashing Magazine, *Meet Utopia* (indexed text)
- Standard Ebooks, *Manual of Style* §8 Typography — github.com/standardebooks/manual (`8-typography.rst`)
- Huerta Tipográfica / Font Squirrel / KREATIV on Alegreya's design intent and ATypI Letter.2 (indexed text)
- Craig Mod, *A Simpler Page* (A List Apart) and Bibliotype — github.com/cmod/bibliotype; craigmod.com (indexed text)
- gwern, *Design of This Website*; gwern.net repository README — github.com/gwern/gwern.net (indexed text and README)
- Andy Bell, *CUBE CSS*; *Build Excellent Websites*; Piccalilli (indexed text)
- Studio Airport / Emergence Magazine: It's Nice That interview; Emergence "Behind the Scenes of Our Design Process"; Webby, One Club and Awwwards listings (indexed text)
- Aeon Media press release, *Aeon Media Relaunches Psyche.co* (May 2025); Liquorice case study (indexed text)
- Responsive Web Design podcast, *Lapham's Quarterly*; Dillon Sturtevant redesign notes (indexed text)
- Plough, *Retooling the Plough*; Ekstasis, *Our Story*; Christianity Today announcement (indexed text)
- Creative Boom / Creative Bloq / Design Week on The Guardian's 2025 redesign (indexed text)
- Mobile typography guides: adoc-studio, We Are Affective, FrontendTools, DeveloperUX (2025) (indexed text)
- Pull-quote guidance: River, Number Analytics, Columbia visual identity (indexed text); drop-cap conventions: ebookpbook, Cambric (indexed text)

**Imagery**
- Meltwater, *What the Rise of AI Slop Means for Marketers*; CNN Business, *Why 2026 could be the year of anti-AI marketing*; Digiday on authenticity; Fortune; TechRadar (indexed text)
- Creative Boom, *Six surprising illustration trends for 2026*; Creative Bloq, *Messy, meaningful and made by humans*; Studio 2am, *Naive, grainy and blurred on purpose*; It's Nice That, *Graphic trends 2026*; ArtCoast, *Halftone & Neo-Print 2026* (indexed text)
- Fast Company / Design Week / Brand New on Collins' 2015 Spotify identity and duotone (indexed text)
- Public Domain Review and Public Domain Image Archive coverage: It's Nice That, Colossal, Creative Boom (Jan 2025) (indexed text)
- Rijksmuseum: Fabrique and Q42 case studies; Dutch Design Awards; 2025 Webby listing (indexed text)
- Open-access sources: Met Open Access; Cleveland Museum of Art Open Access; Walters Ex Libris / Digital Walters; Dumbarton Oaks Byzantine Collection; Getty Open Content; Wellcome Collection; Princeton Index of Christian Art (indexed text)
- Grain technique and performance: freeCodeCamp, Codrops, ibelick, Ultimate Design Tools (indexed text)

**Theming**
- Flexoki — github.com/kepano/flexoki (README, fetched); stephango.com/flexoki (indexed text)
- Level Access, *Astigmatism and Web Accessibility*; Stéphanie Walter, *Dark mode & accessibility myth*; WebAIM guidance (Apr 2025) as cited (indexed text)
- Radix Colors documentation (Sand/Bronze scales, APCA) (indexed text)
- Bryce Wray, *It's tri-state switch time* (2024); Tamas Piros; Lexington Themes (2025) on three-state toggles (indexed text)
- Apple Support on Books themes; Windows Report on Chrome Reading Mode sepia themes (indexed text)

**Mobile**
- Nielsen Norman Group, *Mobile Content Is Twice as Difficult*; *Reading Content on Mobile Devices*; UX Magazine, *Why Reading on Mobile Is Uniquely Challenging* (2026) (indexed text)
- The Pudding, *Responsive scrollytelling best practices* (indexed text)
- WCAG 2.2 SC 2.5.8 explainer pages; Apple HIG / Material target sizes (indexed text)
- iOS 26 Safari sticky/fixed regression reports; `dvh` guidance (indexed text)
- Web Almanac 2025 font-loading data as cited by Font Compressor / corewebvitals.io (indexed text)
