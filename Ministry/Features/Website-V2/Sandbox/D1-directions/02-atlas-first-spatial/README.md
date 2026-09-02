# D1 Direction 02 — Atlas-First Spatial

**Sandbox artifact, D1 diverge phase. Not a deliverable; not converged; not softened toward any other direction.** Files: `homepage.html` (the working mockup), `journey.html` (the key inner journey, eight beats), this README.

## 1. The philosophy

The homepage is the map. Not a map on the homepage — the page a first-time visitor lands on *is* twenty centuries of the Church on one canvas, and the visitor orients the way you orient in a place: by looking, then walking. Time runs downward (the live Atlas's own model); west is left, east is right, so the seven Representatives sit where and when they lived — Chloe's house-churches a wide band from Antioch to Rome at the top, Theon in Alexandria beneath and east, Albina's circle setting out from a pin at Rome and landing at Bethlehem. The threads between them are only the ones the census carries, confidence in words. Eras III–X are bands with their real counts and real status — surveyed, on record, none built yet — so "twenty centuries" is literally true on the page and the honesty about what isn't built is structural.

There is no Home/About/Support hierarchy. A conversation is entered by discovering a stop: hover for a glimpse, click for the full entry, and inside it the two doors the launch ruling already defined (Interview, and the quieter Bring-to-the-Table). About and Get Involved are plates on the same canvas — "how to read this" at the top, "the edge of the map" past the last band — reached by scrolling, not leaving. The nav is three words and a toggle.

The bet: a spatial, chronological canvas tells this project's story — many movements, one origin, threads only where the record allows, plans shown as plans, closed doors with grounds stated — faster and more truthfully than any paragraph, before the visitor has read a word.

## 2. Against the four charter goals

**Accessibility.** A map-first direction fails by construction if the spatial layer is the only layer: position, color, and drawn lines are exactly what a screen reader, a keyboard, 300% zoom, or a colorblind visitor cannot use. So the direction's own law is: *the map is a view of a document, never the document.* The DOM is an ordered list of eras, each an ordered list of stops, chronological; CSS positions it spatially only above 900px. Every stop is a real button whose accessible name states name, title, tradition, dates, places, status. Every thread's type, confidence, and note are repeated as sentences in both entries it joins. Focus does what hover does; arrow keys walk the timeline; the Level-3 panel is non-modal on desktop, closes on Escape, returns focus. "Read as a list" removes the spatial layer on any screen. Below 640px the list form is the only form — the constitution's era-accordion, a different form, not a shrink. A live badge names the era under the viewport. What stays hard, said plainly: a visitor who wants one "start" button gets a map; pointers with no hover state see nothing until they tap; the "everything hangs from the top band" picture is carried by words once the canvas collapses. `journey.html` lists these for D2.

**Clear storytelling.** The four messages are told by shape. *The whole Church in the open:* ten eras, 292 entries counted, seven houses. *It shows its work:* the legend is the thesis, dashed means contested, the Reformation band says the count is set and the names aren't chosen. *Witness, never recruitment:* closed doors with grounds stated, exclusion never a judgment. *The build is the product:* the two dashed plans at Carthage are the next builds; the ask sits at the map's edge, quiet.

**Easy access to features.** Every Representative is one hover and one click from landing, both hand-offs inside the entry and placed *above* the long reading, so a decided visitor never scrolls past two thousand words to find the chair. Deep links (`#alexandria-catechetical`) make every stop a sendable place. The cost: no search on the homepage — right at seven stops, wrong past a dozen, when search returns to the plate as a build rule.

**Professional, cutting-edge design.** A restrained cartographic instrument — approved era grounds, one sticky plate, threads at half strength until asked, motion only for the mark and the panel's slide — reads as serious digital humanities and is unmistakably this project's.

## 3. What it deliberately sacrifices

- **The hero and CTA stack.** Nothing says "start." If the bet is wrong, it's wrong at the front door.
- **Page-level IA.** About and Get Involved survive as plates and deeper reads (`about.html`, `support.html` remain) but leave the nav. A search arrival for "who runs this" lands on a map.
- **The 283 unbuilt entries** are counts and bands here, not stops; `atlas-v3.html` keeps them all, with search and filters.
- **Some Table-primacy.** The constitution keeps the in-app map on-request; this site opens *on* the map (§7).
- **Engineering weight.** Two forms, data-derived positions, threads redrawn on resize.

## 4. Typography, color, motion — inside the locked system

Alegreya for reading and the wordmark (italic *in*), Alegreya Sans for chrome; nothing under 13px carries meaning. Madder is the action accent (Interview, focus rings, nav underline); gold-leaf is the witnesses' pigment (the panel's rule, threads, section labels); world tints appear only as rings, left-rules, portrait borders — never as text on a ground. Links on an era ground are ink with a madder underline. Motion: the mark builds once; the glimpse has no transition; the panel slides 220ms; `prefers-reduced-motion` stills everything. No pan, no zoom, nothing moves to attract a click.

## 5. The Atlas palette debt — paid down, with the math

D0 §2.C named it: the live Atlas runs `--bg:#f3ecdc`, `--gold:#83662a`, `--ink:#3a3020`, Georgia. A direction that makes the Atlas the homepage cannot inherit that. So `homepage.html` *is* the converged palette: chrome on the brand tokens, era bands on the **ten approved grounds** from the Icon & Table Template Spec §7 (`#EFDDB3` → `#DEE7EC`; dark `#241A0C` → `#141A20`), Alegreya throughout. In D3, `atlas-v3.html` adopts this token block.

Two seams found while paying it:

1. **`world-census.json`'s `ground`/`groundDark` don't match the approved table** — the census cycles three values across eras II–X, so the live Atlas shows non-approved grounds today. A data fix, whichever direction wins.
2. **`--muted` (`#6B6259`) fails AA as text on the Era I ground: 4.45:1.** So does gold-leaf on any ground (3.75–4.00) and four of seven world tints (Chloe 4.25, Papnoute 4.08, Chilo 4.19, Mar Yausep 3.75). Proposed token: `--ink-faded-ground: #4A433C` for secondary text on a ground — 7.25:1 on Era I, ≥7.2 on all ten (dark `#B8AEA1`, ≥7.8). Tints as non-text rings clear 3:1 everywhere (worst 3.75); white on every tint fill clears 4.5 (worst 5.02); iron-gall on every ground ≥11.3; madder as focus ring ≥4.84; dark-mode madder `#E08C74` ≥6.6.

Deferred, with reason: reconciling the seven carousel tints with the Atlas's thirteen family hues (Chloe is violet on one, brown on the other) — constitution §10.2 already owns it; this direction uses the carousel's tints because they're visitor-facing today.

## 6. Accessibility floor

**WCAG 2.2 AA site-wide, plus three AAA criteria binding for the map region, plus one rule stronger than any criterion.**

- **1.4.6 Enhanced contrast (7:1) for text on era grounds.** The site's two shipped-then-caught contrast bugs were on tinted surfaces, and this direction puts most of its text on them; 7:1 survives a hand-nudged ground.
- **2.4.8 Location.** A canvas without "where am I" is where non-visual and low-vision visitors get lost: the year badge, sticky era heads, and the region summary make it binding.
- **2.4.13 Focus appearance** — 2px madder, offset, ≥4.8:1 on every ground.
- **The equivalence rule:** every fact conveyed by position, color, or a drawn thread is stated in words in the DOM. Auditable — remove the CSS and nothing is lost.

Also held: 2.5.8 target size (≥44px), 2.5.7 (no drag-only interaction), 2.4.11 (plates never obscure focus), 1.4.10 reflow (no horizontal scroll at any width).

## 7. Proposed stretches, for Mark to rule on

1. **The site opens on the map.** The constitution (§5.2, §6) keeps the *in-app* map on-request, never auto-opened — a Table-primacy rule for the app. This direction argues the marketing site is a different room: there is no Table on it, so the map is the doorway, not a rival to the encounter (Article 34, "a doorway, not a home"). The grammar inside the map is unchanged.
2. **The mark's sentence sits on the thesis plate** beside a 56px mark; the sticky plate carries the wordmark alone ("lead with it wherever words fit"). The mark appears once, so the dot is never duplicated.
3. **`--ink-faded-ground`** as a named token (§5); the alternative, iron-gall for all text on grounds, flattens hierarchy.

## 8. Not done, by design

No historical-site photos (rights unresolved). Portraits load from the live site by relative path and degrade to a tinted initial. "Tour" appears nowhere. The cost line carries no figures — D0's volatile slot — with the live Stripe links and the entity sentence verbatim. The homepage only ever suggests one seat; the multi-seat gate (D0 §2.G) stays unconfirmed. Cappadocian is the seventh house because the census says so; `whats-next.html` still disagrees.
