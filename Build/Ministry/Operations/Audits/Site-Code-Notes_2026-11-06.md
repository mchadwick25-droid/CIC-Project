# Public site — code notes lifted out of the live files (2026-11-06)

The comments that sat inside the public site's pages, scripts and stylesheets, moved here so
the live files carry only code (Mark, 2026-11-06: "no notes, keep in a separate file … clean
the rest in a separate PR"). The map's own notes are in
`Build/Ministry/Features/Church-Family-Tree/Code-Notes_2026-11-06.md`. Two kinds of comment
stayed in the files, because code reads them as markers: `<!--SECTION:…-->` blocks and the
`BEGIN`/`END orientation-content-css` lines, both found by
`Build/tools/generate_tradition_pages.py`. Line numbers point into the cleaned files at the
commit that made this file; search for the quoted code if they have moved. Each note is the
comment's own text, joined onto one line.

## `cic-website/_headers`

- **Top of file**: Cloudflare static-asset headers. Pages and data are never cached, so every visitor gets the current version after a deploy. Assets have unhashed filenames and are edited in place, so they get a short cache, not a long or immutable one. Every response carries the baseline security headers. There is no frame-blocking header, because talk.html frames the app.

## `cic-website/assets/chooser.js`

10 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 93** (`var helpId = "chooser-help-" + mode;`): ---------- deck controls ----------
- **Line 126** (`var hand = el("div", { class: "chooser-hand", role: "group", "aria-roledescription": "hand`): ---------- hand ----------
- **Line 146** (`var seatsEl = el("ul", { class: "seats", "aria-label": "On your table" });`): ---------- tray ----------
- **Line 164** (`function talkHref(ids, m, source) {`): ---------- links ----------
- **Line 169** (`var ICON_TALK = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4`): ---------- cards ----------
- **Line 232** (`function startNarration(card) {`): Called only from the tap or key press that turns a card, so the browser
- **Line 232** (`function startNarration(card) {`): counts it as the person's own start. A refusal leaves the Listen button as it was.
- **Line 319** (`function eraName(w) { var e = eras[w.era]; return e ? e.name : ""; }`): ---------- deck: filtering, dealing, search ----------
- **Line 464** (`function toggleSeat(id) {`): ---------- seats and tray ----------
- **Line 506** (`var narrowMq = matchMedia("(max-width: 699px)"), rmMq = matchMedia("(prefers-reduced-motio`): ---------- list fallback ----------

## `cic-website/assets/feedback.css`

7 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 2** (`.feedback-toggle {`): "Tell us what you think": the header button and the card it opens. Linked on every page, including those with their own inline styles, so the colours here are the site's dark palette written out directly.
- **Line 24** (`.site-header > :has(> .feedback-toggle) .feedback-toggle { margin-left: auto; }`): Site header: the button sits beside Menu, at the right end of the row.
- **Line 36** (`.topbar .feedback-toggle { white-space: nowrap; }`): Church Family Tree bar: the button takes the look of the Reset button.
- **Line 38** (`.bar .feedback-toggle { min-height: 36px; padding: .35rem .9rem; font-size: .8rem; }`): Conversation page bar: the button sits at the right end.
- **Line 43** (`.feedback-card {`): The card. Fixed below the bar that holds the button, so it opens in view on every page layout.
- **Line 162** (`.page-feedback {`): Page like and report: the quiet row at the foot of a Church Family Tree page, and on the interactive tree a small bar fixed at the bottom centre.
- **Line 262** (`.page-feedback--fixed {`): Interactive tree: a small bar fixed at the bottom centre, below the legend and the zoom hint in stacking order; on a narrow screen it rides above their row. The card opens upward.

## `cic-website/assets/feedback.js`

3 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 1** (`(function () {`): "Tell us what you think": opens a card from the button with id feedback-toggle and posts the comment to the engine. On Church Family Tree pages and the interactive tree it also adds a quiet row at the foot of the page: a like, and a link that opens a small card to report a problem. The card is added to the page when the script runs. With JavaScript off the button does nothing and the Contact link in the footer still works. The engine address follows the same local-or-live rule as go-deeper-config.js, worked out here so the script stands alone.
- **Line 281** (`} catch (e) {  }`): storage blocked: the like still works for this visit
- **Line 288** (`try { window.localStorage.setItem(LIKE_KEY, '1'); } catch (e) {  }`): remembering is a convenience

## `cic-website/assets/go-deeper-config.js`

6 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 3** (`var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;`): The two addresses the Go Deeper pages talk to, in one place. The app's own
- **Line 3** (`var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;`): VITE_DEEPER_SITE_ORIGIN and the server's CIC_DEEPER_SITE_ORIGIN must name
- **Line 3** (`var isLocal = ["localhost", "127.0.0.1"].indexOf(root.location.hostname) !== -1;`): this site's exact origin.
- **Line 4** (`root.GoDeeperConfig = {`): Off, the privacy page keeps its Go Deeper section hidden.
- **Line 6** (`accounts: true,`): On when accounts are open; off, the privacy page keeps its account sections hidden.
- **Line 7** (`pilot: true,`): On when a pilot audience is open; off, the pilot page shows nothing.

## `cic-website/assets/go-deeper.js`

10 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 90** (`function handOff(opener, codes, appOrigin) {`): Hands the code to the conversation that opened this window, if it is still
- **Line 90** (`function handOff(opener, codes, appOrigin) {`): there, to that one origin only. The caller shows the code regardless.
- **Line 100** (`function returnUrl(appOrigin, reference) {`): The address carries the reference, never the code: a reference stops
- **Line 100** (`function returnUrl(appOrigin, reference) {`): working when the server's hour ends, so a copy left in browser history
- **Line 100** (`function returnUrl(appOrigin, reference) {`): is dead soon after. The app asks before using it.
- **Line 104** (`function deliver(codes, env) {`): Gets one code into the buyer's conversation without a paste. First the
- **Line 104** (`function deliver(codes, env) {`): window that opened this one, which answers once it has saved the code;
- **Line 104** (`function deliver(codes, env) {`): if nothing answers, or there is no such window, this window goes to the
- **Line 104** (`function deliver(codes, env) {`): app with the code in the address fragment, which the app reads and clears
- **Line 104** (`function deliver(codes, env) {`): at once. A pack of several codes is left on the page to share out.

## `cic-website/assets/narration-player.js`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 1** (`(function () {`): Narration player: a typographic play control, a seekable rail, the time and a speed choice, drawn over each page's own <audio> element. The <audio> stays in the page and does all the playing, so anything that already starts, stops or reads it (the Atlas panel's autoplay, the pause-the- others rule) keeps working, and a browser without JavaScript keeps the ordinary controls. The speed is one setting for the whole site, remembered in this browser.
- **Line 55** (`} catch (e) {  }`): the choice then lasts for this page only
- **Line 127** (`if (go && go.catch) go.catch(function () {  });`): the browser refused; the button stays as it was
- **Line 167** (`document.addEventListener('play', function (e) {`): One voice at a time across the page.

## `cic-website/assets/orientation-render.mjs`

53 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 2** (`export function escapeHtml(s) {`): Shared renderer: world_front-compiled JSON (engine.m2.site_compiler's output, cic-website/data/worlds/<census_id>.json) -> participant-facing HTML fragments. Website V2 world_front design, approved to proceed, site cutover stage. This is the ONE place the Orientation-tier content (story/documented_stories/voices/floor_note/legacy/relations_summary/ sourcing/read_first) and the Narrative-tier content (who_speaks/quiet/ questions/glossary/pull_quotes) turn into HTML, so the Atlas panel (cic-website/atlas-v3.html, fetched at runtime for the 8 built worlds) and each static tradition page (cic-website/traditions/<slug>.html, generated once by Build/tools/generate_tradition_pages.py, which runs this same file through Node) can never quietly drift apart into two independently-maintained templates - the exact anti-pattern this design exists to retire. Plain ES module, no build step: runs unmodified in a browser via `<script type="module">` and in Node via `import`/`node --input-type=module`. No DOM access anywhere in this file - every function returns an HTML string, so it works the same in both environments.
- **Line 30** (`function highlighter(compiled) {`): A world's orientation.highlights, applied to one stretch of reading (the
- **Line 30** (`function highlighter(compiled) {`): story, or one documented story's telling): each phrase is marked at its
- **Line 30** (`function highlighter(compiled) {`): first appearance in that stretch only, longest phrase first, never inside
- **Line 30** (`function highlighter(compiled) {`): another mark. The note shows on hover, on keyboard focus, and on tap
- **Line 30** (`function highlighter(compiled) {`): (a tap focuses the mark), with no script.
- **Line 67** (`function figureName(figure) {`): A figure's own in-world name (falls back to the first name entry, then
- **Line 67** (`function figureName(figure) {`): the record id) - never the parenthetical scholarly form, which belongs
- **Line 67** (`function figureName(figure) {`): in a hover/detail context, not as a figure's headline name here.
- **Line 86** (`function narrationPlayer(url) {`): ---- Orientation tier (shared between the Atlas panel and a tradition page) ----
- **Line 86** (`function narrationPlayer(url) {`): A narration player for one clip. `url` is null/absent when no audio exists
- **Line 86** (`function narrationPlayer(url) {`): for the piece, in which case nothing is drawn.
- **Line 95** (`export function renderStory(compiled, opts) {`): opts.narration = { story: url, legacy: url, documented: { [story_id]: url } },
- **Line 95** (`export function renderStory(compiled, opts) {`): built by the caller from cic-website/audio/worlds/manifest.json.
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): title/when/teaser are always visible - only the story's own telling
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): (its tellable_as where it has no telling yet) sits behind the
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): disclosure. Reuses atlas-v3.html's own docstory-item/docstory naming convention for visual consistency,
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): but not its exact hide/show split: the Atlas panel's own pre-existing
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): pattern puts the teaser behind a hover tooltip on the collapsed
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): summary, while this shared renderer (used by both surfaces, so they
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): can't drift apart) keeps the teaser always in view per this content
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): design's own explicit rule - a deeper click is for the full account,
- **Line 124** (`export function renderDocumentedStories(compiled, opts) {`): not for the one-line hook that gets a reader there.
- **Line 186** (`export function renderWhoSpeaks(compiled) {`): ---- Narrative tier (tradition-page-only sections) ----
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): A `cite` entry resolves to a full record's own content field (a
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): doctrinal_witness's `text`, an honest_limit's `statement`, etc - see
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): engine/m2/site_compiler.py's own _CITE_TEXT_FIELD_BY_TYPE), not a short
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): bibliographic locus, so there is no citation string in the compiled data
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): to reproduce verbatim here. Rendered instead as a short, honestly-
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): labeled excerpt of the record that actually grounds the question -
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): never invented, never a fabricated citation form. The cut favors a
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): sentence boundary within `maxLen` over an arbitrary word-boundary
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): chop, so the excerpt reads as a complete thought rather than trailing
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): off mid-clause; only when no sentence end falls in range does it fall
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): back to the nearest word boundary. See this generator's own report for
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): this judgment call.
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): Most record_type values already read fine to a participant once
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): underscores become spaces ("contested_claim" -> "contested claim").
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): "gravity" is this project's own internal term (Doc_04 Gravity
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): Discovery - a world's core theological conviction) and reads as
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): jargon on its own, so it gets an explicit participant-facing label
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): here rather than a hand-edited copy of the citation text, which
- **Line 198** (`const RECORD_TYPE_LABELS = { gravity: "core conviction" };`): would only need doing again on every recompile.
- **Line 249** (`export function renderPullQuotes(compiled) {`): A quote's own `speaker_or_author` arrives already resolved to a
- **Line 249** (`export function renderPullQuotes(compiled) {`): readable name - engine/m2/site_compiler.py's _resolve_quote() runs it
- **Line 249** (`export function renderPullQuotes(compiled) {`): through citation_cards.py's own figure-label lookup at compile time, so
- **Line 249** (`export function renderPullQuotes(compiled) {`): there is nothing left for this renderer to unwrap.
- **Line 261** (`export function narrationUrls(entry, base) {`): The narration URLs for one world, from its entry in audio/worlds/manifest.json;
- **Line 261** (`export function narrationUrls(entry, base) {`): `base` is the path from the calling page to audio/worlds/ (with trailing slash).
- **Line 272** (`export const RENDERERS = {`): Every render function this module exports, keyed by name - the single
- **Line 272** (`export const RENDERERS = {`): list a Node CLI wrapper (Build/tools/render_orientation_cli.mjs) and the Atlas
- **Line 272** (`export const RENDERERS = {`): panel's own runtime import both iterate/select from, so a new section
- **Line 272** (`export const RENDERERS = {`): added here needs no separate registration anywhere else.

## `cic-website/assets/pilot.js`

6 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 4** (`var LINK = /^[A-Za-z0-9_-]{1,64}$/;`): A public audience's name or a private audience's secret key. The page cannot tell which, and does not need to.
- **Line 6** (`function linkOf(search) {`): The link a page address names (?for=...), or general when it names none. Other parameters are ignored.
- **Line 12** (`var ROLE = /^[a-z_]{1,32}$/;`): One of the join form's role values. The server holds the list and checks it.
- **Line 14** (`function joinUrl(appOrigin, link, role) {`): The app's address for the pack: the link and the chosen role travel in the fragment, which no server is sent.
- **Line 26** (`if (root.location.search && root.history && root.history.replaceState) root.history.replac`): A private audience's key is a password: it leaves the address bar and the history at once, before anything else can return.
- **Line 27** (`if (!config.pilot || !link) return;`): Nothing shows until the pilot is opened in the site's config, so a link found early shows an empty page.

## `cic-website/assets/privacy-go-deeper.js`

3 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 4** (`function apply(doc, config) {`): Shows the Go Deeper parts of the privacy page only when Go Deeper is on,
- **Line 4** (`function apply(doc, config) {`): and swaps the one-job cookie paragraph for the two-job one.
- **Line 16** (`var ACCOUNT_PARTS = [`): The account parts of the page, shown only when accounts are on. Independent of Go Deeper.

## `cic-website/assets/style.css`

13 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 2** (`:root {`): Church in Conversation — public site stylesheet Brand system: CiC_UX_Design_Brand_Brief_V1_0.md / Messaging & Branding Kit V0.2
- **Line 55** (`header.site-header {`): Header
- **Line 77** (`.arriving-mark svg { display: block; width: 34px; height: 34px; }`): "Arriving" mark motion — Logo & Motion Brief V1.0 (Build/Ministry/Technology). Binding: plays once per page arrival, then the breath continues; the dot never enters the ring; no interaction reacts to the cursor.
- **Line 114** (`.menu { position: relative; margin-left: auto; }`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 60rem width.
- **Line 115** (`@media (min-width: 1000px) {`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 141** (`nav.site-nav {`): top: 100% with zero gap to the button, margin-top for the visual gap instead -- any gap via `top` alone is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges that margin-top gap so :hover survives the crossing.
- **Line 173** (`.hero {`): Hero
- **Line 223** (`.narration { display: flex; align-items: center; gap: .55rem; flex-wrap: wrap; margin: .3r`): Sections
- **Line 256** (`ol.convictions {`): Convictions list
- **Line 289** (`.callout {`): Callout / status box
- **Line 309** (`.worlds-strip {`): World strip on home
- **Line 352** (`footer.site-footer {`): Footer
- **Line 377** (`a, .hero .eyebrow, .page-section .eyebrow, .btn.secondary,`): --madder/--gold-leaf stay unchanged (button fills need the darker value for contrast against light text) - these overrides lighten the SAME hues only where they're used as text/border color on the near-black background.

## `cic-website/atlas.html`

1 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 16** (`<p>This page is now <a href="atlas-v3.html">Church Family Tree</a>.</p>`): This page has moved: the Story surface merged into Church Family Tree (Blueprint B5.g, the ship flip; renamed from "Church in History"). Kept as a redirect stub rather than deleted so existing links and bookmarks still land.

## `cic-website/go-deeper.html`

2 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 166** (`var PAYMENT_LINKS = {`): Each pack's Stripe Payment Link (https://buy.stripe.com/...) is set here when sales open.
- **Line 166** (`var PAYMENT_LINKS = {`): A pack with an empty link is not shown; the page stays closed until one link is set.

## `cic-website/index.html`

18 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 66** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four items together don't fit one row at the page's own 1024px header width -- verified by measuring rendered widths directly rather than guessing (brand+features+menu-trigger ~957px fits; the same row with the nav's four links spelled out inline would run to ~1250px).
- **Line 75** (`@media (min-width:62.5rem){`): Centered in the space actually available between the logo and the menu button, not just "centered in whatever's left over" (equal flex-grow on .brand/.menu fails because the wordmark's fixed width wins a floor against flex-shrink, so the two sides end up unequal) and not naive full-row-width centering either (that ignores brand and menu's own widths entirely and visually collides with the wordmark, since brand is wider than menu). Grid's max-content/1fr/max-content sizes the outer two columns to brand's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 84** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. Touching boxes keep :hover continuous all the way down.
- **Line 108** (`.feature-card{margin:3rem 0 0;background:var(--surface);border:1px solid var(--rule);borde`): .feature-card: the bordered container shared by the Church Family Tree and Conversation with One.
- **Line 115** (`.atlas-showcase{max-width:calc(var(--wide) - 2.5rem);margin-left:auto;margin-right:auto}`): Church Family Tree showcase: a slow, one-time scrolling pan (era 1 -> 10) with the text sitting below it in a plain solid block rather than overlaid -- overlaid text on a moving, multicolored map risks unpredictable contrast frame to frame, which this site's own accessibility bar (WCAG-checked throughout) doesn't accept on a guess. prefers-reduced-motion swaps in the existing static atlas-preview.jpg instead of the video. Narrowed to the width of the text column and capped in height so it reads as a narrow window looking in on the map, not a full-bleed banner. A .feature-card itself, matching the same var(--wide)-less-2.5rem column the chairs gallery and Unfolding Story already use -- video and text don't need their own separate width-matching math since the card they both sit inside carries it.
- **Line 116** (`.atlas-showcase-media{position:relative;display:block;width:100%;height:min(42vh,336px);ov`): Short enough that the title of Church Family Tree lands on the first screen when the landing page loads. Flush at the top of the card (no side width-matching math of its own, no border of its own -- the hover affordance is a slight zoom instead, since a border here would sit oddly against the card's own rounded top corners).
- **Line 187** (`.support-photo{flex:1;aspect-ratio:16/10;min-height:60px;margin:0 0 .9rem;padding:.5rem;bo`): Fills whatever blank space the card's own stretched height (matching the Table card beside it) leaves below the give buttons -- flex:1 rather than a fixed height so it absorbs exactly that space at any card height. aspect-ratio caps it too, fixing a real bug: the photo itself is a tall portrait crop (700x1050), and without a cap, an <img> with height:100% inside this flex item falls back to that native ratio during the browser's own auto-height/intrinsic-sizing pass -- which made the Support card's own natural height balloon past Build a Table's, forcing Build a Table to stretch to match and leaving a ~300px dead gap above its own CTA link. The ratio still allows flex:1 to grow it taller than this when the Table card genuinely is taller, same as before.
- **Line 187** (`.support-photo{flex:1;aspect-ratio:16/10;min-height:60px;margin:0 0 .9rem;padding:.5rem;bo`): Inset padding, no background of its own, so the card's own --surface shows through around the photo like a mat/frame rather than the image running edge to edge inside its allotted space.
- **Line 265** (`<video id="atlas-showcase-video" autoplay muted playsinline poster="assets/atlas-preview.j`): Slow pan from era 1 through era 10 on the live Church Family Tree, recorded chrome-free (topbar/feature-bar/scope-note/legend/reset button hidden -- just the map). Ambient, not meant to be read frame-by-frame; the section's own text below carries the explanation. Plays once per page load and resets to its era-1 opening frame afterward rather than resting on era 10 -- see the script below. The whole thing is a link to the Family Tree itself, not just decorative.
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): Plays once (no loop); resting on era 10's own frame afterward read as the
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): section stopping on "the end" rather than the church's whole span -- reset
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): back to the era-1 opening frame instead once playback finishes.
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): Reduced-motion visitors already get the static poster image in place of
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): this video (see .atlas-showcase-media's own CSS), so this listener never
- **Line 328** (`var showcaseVideo = document.getElementById('atlas-showcase-video');`): fires for them.
- **Line 344** (`var menu = document.querySelector('.menu');`): Site nav collapsed into a "Menu" dropdown: :hover in CSS handles the
- **Line 344** (`var menu = document.querySelector('.menu');`): mouse case, this handles keyboard (Enter/Space on the button, then
- **Line 344** (`var menu = document.querySelector('.menu');`): Escape to close) and touch, which don't hover.

## `cic-website/story.html`

1 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 23** (`:focus-visible{outline:2px solid #E08C74;outline-offset:3px;border-radius:2px}`): Page-specific pieces the shared stylesheet doesn't cover: a left-aligned "document" hero (breadcrumb-topped, narrower measure) instead of the shared centered marketing .hero, plus the breadcrumb trail, body-copy column, story-updates box, and back-link only this page uses. Moved onto the shared assets/style.css -- this page's own private copy of the site's header/footer/nav chrome had drifted from it, missing the logo mark entirely, and would keep drifting on every future header change.

## `cic-website/support.html`

2 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 23** (`.fine-print{font-family:'Alegreya Sans',sans-serif;font-size:.95rem;color:#B8AEA1}`): .fine-print replaces two inline style="color:var(--muted)" paragraphs: --muted is never redefined for dark mode anywhere on this site, and an inline color always outranks the shared stylesheet's own .page-section p{color:#B8AEA1} dark-mode rule by specificity - so an inline color silently defeats the fix that's already sitting right there. A real class lets the same dark-mode override apply the way it already does for the rest of this page's text.
- **Line 68** (`<p>Every conversation has a real cost, turn by turn. Multi-voice Table conversations incre`): Deliberately no dollar figure and no itemized cost breakdown here: a specific number reads as the whole cost of running this and invites "how much, exactly," which this page can't honestly answer (server fees, developmental cost, and everything else in Ministry/ carry no measured dollar figure yet). States only that cost is real and per-turn, that real effort has gone into lowering it, that Multi-voice Table conversations add to it since each additional voice generates its own response, and that costs grow with real growth (more traditions, more people) - in general terms only, with no target numbers, since neither a user count nor a world count is a decided public roadmap commitment. See the funding-strategy decision record under Build/Ministry/Features/Funding-Strategy/ for the full revision history.

## `cic-website/table.html`

3 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 51** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 56** (`@media (min-width:62.5rem){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 65** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.

## `cic-website/talk.html`

13 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 33** (`body{margin:0;background:var(--ground);color:var(--text);font-family:var(--sans);display:f`): flex column, not a fixed-height guess for .frame-wrap -- a hardcoded calc(100vh - <bar> - <feature-bar>) here made the same mistake atlas-v3.html's scope-note positioning already had to be fixed for once: the bars' real rendered height (font/line-height/padding, or wrapping on a narrow screen) doesn't match a guessed pixel constant, so the iframe below overflowed the viewport instead of filling it exactly. flex:1 fills whatever's actually left, no measuring needed.
- **Line 109** (`var view = window.visualViewport;`): A phone keyboard shrinks only the visual viewport; size the page to it so
- **Line 109** (`var view = window.visualViewport;`): the framed app's message box stays just above the keyboard. Pinch-zoom
- **Line 109** (`var view = window.visualViewport;`): shrinks the visual viewport too, so a zoomed page keeps its normal layout.
- **Line 121** (`window.addEventListener('message', function(ev) {`): The embedded app's own "Leave for now"/"Begin again" posts this message
- **Line 121** (`window.addEventListener('message', function(ev) {`): instead of navigating itself when inside an iframe, and #back-link
- **Line 121** (`window.addEventListener('message', function(ev) {`): is already this page's own real, styled answer to "where does leaving
- **Line 121** (`window.addEventListener('message', function(ev) {`): go." ev.source restricts to
- **Line 121** (`window.addEventListener('message', function(ev) {`): exactly our own iframe - the only page that ever loads inside it is the
- **Line 121** (`window.addEventListener('message', function(ev) {`): one this script just pointed at target above.
- **Line 127** (`window.addEventListener('message', function(ev) {`): Once the conversation has started, the app's own bar (portrait and names)
- **Line 127** (`window.addEventListener('message', function(ev) {`): is the only thing above the transcript; "Leave for now" and "Tell us what
- **Line 127** (`window.addEventListener('message', function(ev) {`): you think" sit under the app's message box.

## `cic-website/templates/tradition.html`

2 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 1** (`blocks drop whole when a tradition has nothing for that section. {{RAIL}} is`): Article content for a tradition page. Build/tools/generate_tradition_pages.py fills it and splices it into the <div class="article"> block of each page; everything else on the page (head, header, hero, door, footer, script) is the page's own chrome. {{TOKEN}} is a section's rendered HTML. <!--SECTION:key
- **Line 68** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/alexandria-catechetical.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/cappadocian-nicene-pastoral-monastic-tradition.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/desert-monasticism.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/donatism.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/gallic-monastic-ascetic-christianity.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/hieronymian-ascetic-literary.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/imperial-juridical-christianity.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/latin-pastoral-congregational-christianity.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 164** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/lutheran-wittenberg-and-its-congregations.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 164** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/post-apostolic-house-church.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/syriac-edessa-nisibis.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/traditions/the-reformed-cities-zurich-and-geneva.html`

4 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 42** (`.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}`): Logo, wordmark, the three feature buttons, and the site nav all in one row: the nav collapses into a "Menu" dropdown since all four don't fit alongside the rest in one row at this header's own 1024px width.
- **Line 47** (`@media (min-width:1000px){`): Centered in the space actually available between the logo and the menu button, not naive full-row-width centering (that ignores the wordmark's and menu button's own widths and can visually collide with the wordmark). Grid's max-content/1fr/max-content sizes the outer two columns to the wordmark's and menu's own content exactly, so the middle column is whatever's genuinely left, with no risk of overlapping either side -- only turned on above the width where the whole row fits unwrapped.
- **Line 56** (`.site-nav{font-family:var(--sans);font-size:.9rem;position:absolute;right:0;top:100%;margi`): top:100% with zero gap to the button, not top:calc(100% + Xrem) -- any real gap is a dead zone the pointer crosses with no element under it, which drops :hover before the pointer reaches the menu. The ::before bridges the .5rem visual gap so :hover survives the crossing while keeping the breathing room.
- **Line 155** (`:root{--gold:#D9B35C}`): Wide layout: the page is about the tradition and fills the screen.

## `cic-website/world-atlas.html`

1 notes. Each names the code line it stood above or beside, by its line in the cleaned file.

- **Line 16** (`<p>This page is now <a href="atlas-v3.html">Church Family Tree</a>.</p>`): This page has moved: the Wall Chart + Research Table surfaces merged into Church Family Tree (Blueprint B5.g, the ship flip; renamed from "Church in History"). Kept as a redirect stub rather than deleted so existing links and bookmarks still land.
