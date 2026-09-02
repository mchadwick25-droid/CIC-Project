# D1 Direction 02 — Atlas-First Spatial

**Sandbox artifact, D1 diverge phase. Not a deliverable; not converged; not to be softened toward the others.** Files: `homepage.html` (the working mockup — open it in a browser), `journey.html` (the key inner journey, eight beats), this README.

## 1. The philosophy

The homepage is the map. Not a map on the homepage, not a hero with a map link under it — the page a first-time visitor lands on *is* twenty centuries of the Church laid out on one canvas, and the visitor orients the way you orient in a place: by looking around, then walking. Time runs downward (the live Atlas's own decided model); west is left and east is right, so the seven Representatives sit where and when they actually lived — Chloe's house-churches as a wide band from Antioch to Rome at the very top, Theon in Alexandria beneath it and to the east, Mar Yausep at Edessa on the far right, Albina's circle setting out from a pin at Rome and landing at Bethlehem. The threads between them are only the ones the census carries, with confidence in words. Eras III through X are present as bands with their real counts and their real status — surveyed, on record, none built yet — so "twenty centuries" is literally true on the page and the honesty about what isn't built is structural, not a caveat.

There is no Home/About/Support hierarchy. Conversations are entered by discovering a stop: hover for a glimpse, click for the full entry, and inside the entry the two doors the launch ruling already defined (Interview, and the quieter Bring-to-the-Table). About and Get Involved are not pages you leave for; they are the plate at the top ("how to read this") and the plate past the last band ("the edge of the map: what's next, how it was made, how to help"). The nav is three words and a toggle. The title plate carries one thing besides the wordmark: where you are.

The direction stakes its whole value on one claim: a spatial, chronological canvas tells the project's story — many movements, one origin, threads only where the record allows, plans shown as plans, closed doors with grounds stated — faster and more truthfully than any paragraph, and it does so *before the visitor has read a word*.

## 2. Against the four charter goals

**Accessibility.** This is where a map-first direction is most likely to fail, and it fails by construction if the spatial layer is the only layer — position, color, and drawn lines are exactly what a screen reader, a keyboard, a 300% zoom, or a colorblind visitor cannot use. So the direction's own law is: *the map is a view of a document, never the document.* Concretely, in `homepage.html`: the DOM is an ordered list of eras, each an ordered list of stops, in chronological order; CSS positions it spatially only above 900px. Every stop is a real button whose accessible name states name, title, tradition, dates, places, and status in words. Every thread's type, confidence, and note are repeated as sentences in both entries it joins. Focus does exactly what hover does. Arrow keys walk the timeline; Home/End jump the map. The Level-3 panel is non-modal on desktop (the map stays reachable), returns focus on close, and closes on Escape. "Read as a list" removes the spatial layer on any screen and is remembered. Below 640px the list form is the only form — the constitution's era-accordion, a different form, not a shrink — so the pinch-zoom trouble the live Atlas went six rounds on doesn't exist here. A live "where am I" badge names the era under the viewport. What remains genuinely hard, stated plainly: a visitor who wants a single "start" button gets a map instead; hover-only pointers with no hover state see nothing until they tap; and the "everything hangs from the top band" picture is carried by the words, not reproduced, once the canvas collapses. `journey.html` §"Where this journey could fail" lists these for D2.

**Clear storytelling.** The four messages are told by shape: *the whole Church in the open* — ten eras, 292 entries counted, seven houses; *it shows its work* — the legend is the thesis, dashed means contested, the Reformation band says the count is set and the names aren't chosen; *witness, never recruitment* — closed doors stated with grounds, exclusion never a judgment; *the build is the product* — the two dashed plans at Carthage are the next builds, and the ask sits at the map's edge, quiet. The Rome→Bethlehem journey line and the origin band are stories a paragraph would take a hundred words to tell.

**Easy access to features.** Every Representative is one hover and one click from landing, with both hand-offs inside the entry and placed *above* the long reading, so a decided visitor never scrolls past two thousand words to find the chair. Deep links (`#alexandria-catechetical`) make every stop a sendable place. The honest cost: no search on the homepage. With seven stops that's right; past roughly a dozen it stops being right, and search must return to the plate (build rule, not a maybe).

**Professional, cutting-edge design that draws people in.** A restrained cartographic surface — approved era grounds, one sticky plate, threads at 42–55% opacity until asked, motion only for the mark (once) and the panel's slide — reads as a serious digital-humanities instrument, and it is unmistakably this project's: nothing else on the web looks like a chair pulled out on a map of the early Church.

## 3. What it deliberately sacrifices

- **The hero and the CTA stack.** No button says "start." The direction bets that a visible chair beats a button; if the bet is wrong, it is wrong at the front door.
- **Page-level IA.** About and Get Involved survive as plates and as deeper reads (`about.html`, `support.html` stay reachable), but they leave the top nav. A search-engine arrival for "who runs this" lands on a map.
- **The 283 unbuilt entries.** They are counts and bands on the homepage, not stops; the full Atlas (`atlas-v3.html`) keeps every entry, its search, and its filters. Two atlas surfaces, one data file — same discipline as today's homepage carousel.
- **Some Table-primacy.** The constitution keeps the in-app map on-request and never auto-opened; this site opens *on* the map. See §7.
- **Engineering weight.** Two forms (canvas and accordion), positions derived from data, threads redrawn on resize. More than a hero; less than the live Atlas already carries.

## 4. Typography, color, motion — inside the locked system

Alegreya for reading and the wordmark (italic *in*), Alegreya Sans for chrome and metadata; nothing below 13px carries meaning. Era numerals in Alegreya small caps. Madder is the action accent (the Interview button, focus rings, the one nav underline); gold-leaf is the witnesses' pigment (the panel's rule, threads, section labels); world tints appear only as rings, left-rules, and portrait borders — never as text on a ground. Motion: the mark builds once and breathes; the glimpse appears with no transition; the panel slides 220ms; `prefers-reduced-motion` stills all of it. No pan, no zoom, no thread-drawing animation, nothing moves to attract a click.

## 5. The Atlas palette debt — paid down, with the math

D0 §2.C named it: the live Atlas runs `--bg:#f3ecdc`, `--gold:#83662a`, `--ink:#3a3020`, Georgia. A direction that makes the Atlas the homepage cannot inherit that — the page would be two brands. So `homepage.html` *is* the converged Atlas palette: chrome on the brand tokens, era bands on the **ten approved grounds** from the Icon & Table Template Spec §7 (`#EFDDB3` → `#DEE7EC`, dark `#241A0C` → `#141A20`), Alegreya throughout, madder for action, gold-leaf for the witnesses' thread. Convergence rule for D3, if this direction is picked: `atlas-v3.html` adopts this exact token block; its family hues stay as the map's meaningful color per the spec ("never compete with the world colors").

Two seams found while paying it:

1. **`world-census.json`'s `ground`/`groundDark` fields do not match the approved table** — the census cycles three values (`#EFDDB3`, `#E3E0CB`, `#D8E4E5`) across eras II–X, so the live Atlas (which reads them) is showing non-approved grounds today. The mockup uses the approved ten; the census needs a data fix regardless of which direction wins.
2. **`--muted` (`#6B6259`) fails AA as text on the Era I ground: 4.45:1.** So does gold-leaf as text on any ground (3.75–4.00), and four of the seven world tints (Chloe 4.25, Papnoute 4.08, Chilo 4.19, Mar Yausep 3.75). Proposed token, for Mark to rule on: `--ink-faded-ground: #4A433C` for secondary text sitting on an era ground — 7.25:1 on Era I, ≥7.2 on all ten (dark: `#B8AEA1`, ≥7.8). Tints as non-text rings on grounds all clear 3:1 (worst 3.75); white on every tint fill clears 4.5 (worst 5.02). Iron-gall on every ground ≥11.3; madder as focus ring ≥4.84 on every ground; dark-mode madder text `#E08C74` ≥6.6.

Deferred, with reason: the world-tint vs. Atlas-family-hue reconciliation (the seven `entry.color` values the homepage carousel uses versus the thirteen family hues the Atlas uses — Chloe is violet on one and brown on the other). Constitution §10.2 already owns this as a branding-thread pass; this direction uses the carousel's tints because they are the visitor-facing ones today, and flags it rather than deciding it.

## 6. Accessibility floor

**WCAG 2.2 AA across the site, plus three AAA criteria adopted as binding for the map region specifically, plus one rule stronger than any criterion.**

- **1.4.6 Contrast (Enhanced), 7:1, for all text on era grounds.** The site's own history — two dark-mode contrast bugs shipped and caught after the fact — happened on tinted surfaces; this direction puts most of its text on tinted surfaces. AA is the floor the tints only just clear; 7:1 is the margin that survives a hand-nudged ground.
- **2.4.8 Location.** A spatial canvas without a "where am I" is where non-visual and low-vision visitors get lost; the year badge, sticky era heads, and the region's own summary make it binding.
- **2.4.13 Focus Appearance** (2px madder, 2–3px offset, ≥4.8:1 on every ground) — a focused stop on a busy canvas must be findable at a glance.
- **The equivalence rule:** every fact conveyed by position, color, or a drawn thread is stated in words in the DOM. This is auditable — remove the CSS and nothing is lost — and it is the one rule that makes the philosophy survivable.

Also held: 2.5.8 target size (all stops and controls ≥44px), 2.5.7 (no drag-only interaction anywhere), 2.4.11 (sticky plates never obscure focus; stops carry scroll margins), 1.4.10 reflow (no horizontal scroll at any width — the canvas collapses, it never scrolls sideways), and `prefers-reduced-motion` honored for every transition.

## 7. Proposed stretches, for Mark to rule on

1. **The site opens on the map.** The constitution (§5.2, §6) keeps the *in-app* World Map on-request, never auto-opened, never reachable from the Table — a Table-primacy rule for the app. This direction argues the marketing site is a different room: there is no Table on it yet, so the map is the doorway, not a rival to the encounter (Article 34, "a doorway, not a home"). The grammar inside the map is unchanged — hover/click, panel-not-modal, era-accordion on phone, legend-as-thesis, first-visit orientation. Asking for the ruling explicitly rather than assuming it.
2. **The mark's sentence sits on the thesis plate**, beside a 56px mark, with the sticky title plate carrying the wordmark alone (the usage sheet: "lead with it wherever words fit"). The mark appears once, so the dot is never duplicated. Worth a look, since first contact is the one place the sentence is mandatory.
3. **`--ink-faded-ground`** as a named addition to the token set (§5). The alternative is iron-gall for all text on grounds, which is legible but flattens hierarchy.

## 8. Dependencies and things not done

The six historical-site photos are not used (rights unresolved). Portraits load from the live site by relative path and degrade to a tinted initial. The Tour word is not used anywhere. The cost line at the edge plate carries no figures — it's the volatile slot the D0 note describes, with the two live Stripe links and the entity sentence verbatim. The homepage only ever suggests one seat, the Atlas's own rule, and the multi-seat gate question (D0 §2.G) is left exactly as unconfirmed as it was. Cappadocian appears as the seventh live house because the census says so; `whats-next.html` still says otherwise, and the copy here reads the census rather than repeating that page.
